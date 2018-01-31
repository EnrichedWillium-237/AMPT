# include "TCanvas.h"
# include "TFile.h"
# include "TGraphErrors.h"
# include "TH1.h"
# include "TH2.h"
# include "TLeaf.h"
# include "TMath.h"
# include "TRandom3.h"
# include "TStopwatch.h"
# include "TString.h"
# include "TStyle.h"
# include "TTree.h"
# include <cmath>
# include <complex>
# include <fstream>
# include <iostream>
# include <vector>

using namespace std;

static const int ncentbins = 14;
static const int cminCENT[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 20,  60};
static const int cmaxCENT[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 20, 60, 100};
static const int NCbins = 14;
static const double centbins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100};
static const int nptbins = 18;
static const double ptbins[] = {0.30,  0.40,  0.50,  0.60,  0.80,  1.00,  1.25,  1.50,  2.00,  2.50,  3.00,
    3.50,  4.00,  5.00,  6.00,  7.00,  8.00,  10.00,  12.00};
static const int netabins = 12;
static const double etabins[] = {-2.4, -2.0, -1.6, -1.2, -0.8, -0.4,  0.0,  0.4,  0.8,  1.2,  1.6,  2.0,  2.4};

//----------------------------------
// Tree variables
//
vector<double> * phi = 0;
vector<double> * eta = 0;
vector<double> * pt = 0;
vector<double> * charge = 0;
double b;
double PsiRP;
double Npart;
double Ncoll;
//----------------------------------

//-- MC inputs
TH1D * phiIN;
TH1D * etaIN;
TH1D * ptIN;
TH1D * bIN;
TH1D * epIN;
TH1D * npartIN;
TH1D * ncollIN;
TH2D * sizevsb;

TH1D * hcent;
double ccutlow[ncentbins];
TH2D * v1true2D[ncentbins];
TH2D * v2true2D[ncentbins];
TH2D * v1raw2D[ncentbins];
TH2D * v2raw2D[ncentbins];
TH2D * qcnt[ncentbins];

TFile * fin;
TFile * fcent;
TFile * fout;

TTree * tree0;
TTree * tree1;

# include "style.h"

Double_t bounds( int ord, double ang ) {
    while (ang >  TMath::Pi()/ord) ang-=TMath::TwoPi()/ord;
    while (ang < -TMath::Pi()/ord) ang+=TMath::TwoPi()/ord;
    return ang;
}

void GetVN()
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    phiIN   = new TH1D("phiIN",   "", 100, -3.5, 3.5);
    etaIN   = new TH1D("etaIN",   "", 100, -6, 6);
    ptIN    = new TH1D("ptIN",    "", 100, 0, 12);
    bIN     = new TH1D("bIN",     "", 200, 0, 24);
    epIN    = new TH1D("epIN",    "", 100, -3.5, 3.5);
    npartIN = new TH1D("npartIN", "", 100, 0, 450);
    ncollIN = new TH1D("ncollIN", "", 100, 0, 2000);
    sizevsb = new TH2D("sizevsb", "", bIN->GetNbinsX(), 0, 24, phiIN->GetNbinsX(), 0, 2e4);
    sizevsb->SetOption("colz");
    for (int cbin = 0; cbin<ncentbins; cbin++) {
        v1true2D[cbin] = new TH2D(Form("v1true_%d_%d",cminCENT[cbin],cmaxCENT[cbin]), "", nptbins, ptbins, netabins, etabins);
        v1true2D[cbin]->SetXTitle("p_{T} (GeV/c)");
        v1true2D[cbin]->SetYTitle(Form("#eta (%d-%d%%)",cminCENT[cbin],cmaxCENT[cbin]));
        v1true2D[cbin]->SetOption("colz");
        v2true2D[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("v2true_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
        v1raw2D[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("v1raw_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
        v2raw2D[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("v2raw_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
        qcnt[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("qcnt_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
    }

    cout << "Retrieving centralities... " << endl;
    fcent = new TFile("hists/Cent.root","read");
    hcent = (TH1D *) fcent->Get("lowEdge");
    for (int i = 0; i<hcent->GetNbinsX(); i++) {
        ccutlow[i] = hcent->GetBinContent(i+1);
    }

    fin = new TFile("../AMPTsample.root");
    cout << "Reading file: ../AMPTsample.root" << endl;
    // fin = new TFile("/rfs/wmcbrayer/AMPT/ampt_string_melting.root");
    // cout << "Reading file: /rfs/wmcbrayer/AMPT/ampt_string_melting.root" << endl;
    tree0 = (TTree *) fin->Get("QWTreeMaker/trV");
    tree0->SetMakeClass(1);
    tree1 = (TTree *) fin->Get("QWHepMCMaker/trV");
    tree1->SetMakeClass(1);
    tree0->AddFriend(tree1);

    tree0->SetBranchAddress("phi",    &phi);
    tree0->SetBranchAddress("eta",    &eta);
    tree0->SetBranchAddress("pt",     &pt);
    tree0->SetBranchAddress("charge", &charge);
    tree0->SetBranchAddress("b",      &b);
    tree0->SetBranchAddress("EP",     &PsiRP);
    tree0->SetBranchAddress("Npart",  &Npart);
    tree0->SetBranchAddress("Ncoll",  &Ncoll);

    Double_t c1[NCbins][nptbins][netabins] = {0};
    Double_t c12[NCbins][nptbins][netabins] = {0};
    Double_t c2[NCbins][nptbins][netabins] = {0};
    Double_t c22[NCbins][nptbins][netabins] = {0};
    Double_t cnt[NCbins][nptbins][netabins] = {0};

    // main event loop
    int nevents = tree0->GetEntries();
    int nextStatus = 5;
    double clck = 0;
    int ievnt = 0;
    TStopwatch * sw = new TStopwatch();
    sw->Start();
    cout << "Entering primary event loop..." <<endl;
    while ( tree0->GetEntry(ievnt++) ) {
        //
        // nevents = 1e6;
        if (ievnt>=nevents) continue;
        //
        if (fmod(double(ievnt+1), nevents/20.)==0) {
            cout << " " << nextStatus;
            nextStatus+=5;

            sw->Continue();
            double elapse0 = sw->RealTime();
            if (nextStatus == 5) clck = elapse0;
            cout << "\tElapse time: " << Form("%3.2f",elapse0) << " seconds";
            cout << "\tEstimated total run time: " << Form("%3.2f",clck*20./60./60.) << " hours" << endl;
        }

        bIN->Fill( b );
        epIN->Fill( bounds(1, PsiRP) );
        npartIN->Fill( Npart );
        ncollIN->Fill( Ncoll );
        sizevsb->Fill( b, phi->size() );
        int cbin = hcent->GetXaxis()->FindBin(b)-1;
        if (cbin>=NCbins) continue;
        // cout<<"b: "<<b<<"\tcbin: "<<cbin<<endl;
        for ( unsigned int i = 0; i<phi->size(); i++ ) {
            double phi_ = bounds(1, (*phi)[i]);
            double eta_ = (*eta)[i];
            double pt_  = (*pt)[i];
            phiIN->Fill( phi_ );
            etaIN->Fill( eta_ );
            ptIN->Fill( pt_ );

            int ebin = v1true2D[0]->GetYaxis()->FindBin(eta_)-1;
            int pbin = v1true2D[0]->GetXaxis()->FindBin(pt_)-1;
            if (ebin>v1true2D[0]->GetNbinsY() || pbin>v1true2D[0]->GetNbinsX()) continue;
            c1[cbin][pbin][ebin] += TMath::Cos(phi_ - PsiRP);
            c12[cbin][pbin][ebin] += pow(TMath::Cos(phi_ - PsiRP),2);
            c2[cbin][pbin][ebin] += TMath::Cos(2*(phi_ - PsiRP));
            c22[cbin][pbin][ebin] += pow(TMath::Cos(2*(phi_ - PsiRP)),2);
            cnt[cbin][pbin][ebin] += 1.;
        }
    }

    for (int cbin = 0; cbin<hcent->GetNbinsX(); cbin++) {
        for (int pbin = 0; pbin<nptbins; pbin++) {
            for (int ebin = 0; ebin<netabins; ebin++) {
                double mult = cnt[cbin][pbin][ebin];
                double nc1 = c1[cbin][pbin][ebin]/mult;
                double nc2 = c2[cbin][pbin][ebin]/mult;

                double muc1 = c1[cbin][pbin][ebin]/mult;
                double varc1 = c12[cbin][pbin][ebin]/mult - pow(muc1,2);
                double sigc1 = sqrt( varc1/mult );
                double errc1 = 0.5*nc1*sigc1/muc1;

                double muc2 = c2[cbin][pbin][ebin]/mult;
                double varc2 = c22[cbin][pbin][ebin]/mult - pow(muc2,2);
                double sigc2 = sqrt( varc1/mult );
                double errc2 = 0.5*nc2*sigc2/muc2;

                v1true2D[cbin]->SetBinContent(pbin+1, ebin+1, nc1);
                v1true2D[cbin]->SetBinError(pbin+1, ebin+1, errc1);
                v2true2D[cbin]->SetBinContent(pbin+1, ebin+1, nc2);
                v2true2D[cbin]->SetBinError(pbin+1, ebin+1, errc2);
                v1raw2D[cbin]->SetBinContent(pbin+1, ebin+1, c1[cbin][pbin][ebin]);
                v2raw2D[cbin]->SetBinContent(pbin+1, ebin+1, c2[cbin][pbin][ebin]);
                qcnt[cbin]->SetBinContent(pbin+1, ebin+1, mult);
            }
        }
        v1raw2D[cbin]->Divide(qcnt[cbin]);
        v2raw2D[cbin]->Divide(qcnt[cbin]);
    }

    fout = new TFile("hists/amptVN.root","recreate");
    fout->cd();
    phiIN->Write();
    etaIN->Write();
    ptIN->Write();
    bIN->Write();
    epIN->Write();
    npartIN->Write();
    ncollIN->Write();
    sizevsb->Write();
    hcent->Write();
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TDirectory * tdcent = (TDirectory *) fout->mkdir(Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]));
        tdcent->cd();
        v1true2D[cbin]->Write();
        v2true2D[cbin]->Write();
        v1raw2D[cbin]->Write();
        v2raw2D[cbin]->Write();
        qcnt[cbin]->Write();
    }


    TCanvas * cinputs = new TCanvas("cinputs","cinputs",1200,600);
    cinputs->Divide(4,2);
    cinputs->cd(1);
    phiIN->SetXTitle("#phi");
    phiIN->Draw();
    cinputs->cd(2);
    etaIN->SetXTitle("#eta");
    etaIN->Draw();
    TPad * padinputs3 = (TPad *) cinputs->cd(3);
    padinputs3->SetLogy();
    ptIN->SetXTitle("p_{T} (GeV/c)");
    ptIN->Draw();
    cinputs->cd(4);
    bIN->SetXTitle("b (fm)");
    bIN->Draw();
    cinputs->cd(5);
    epIN->SetXTitle("#Psi_{RP}");
    epIN->Draw();
    TPad * padinputs6 = (TPad *) cinputs->cd(6);
    padinputs6->SetLogy();
    npartIN->SetXTitle("N_{part}");
    npartIN->Draw();
    TPad * padinputs7 = (TPad *) cinputs->cd(7);
    padinputs7->SetLogy();
    ncollIN->SetXTitle("N_{coll}");
    ncollIN->Draw();
    cinputs->cd(8);
    sizevsb->SetXTitle("b");
    sizevsb->SetYTitle("Multiplicity");
    sizevsb->Draw();
    cinputs->Print("figures/AMPT_inputs.png","png");
    fout->cd(); cinputs->Write();


    //fout->Close();

}
