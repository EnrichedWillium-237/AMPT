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

// static const int ncentbins = 14;
// static const int cminCENT[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 10,  70};
// static const int cmaxCENT[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 10, 70, 100};
// static const int NCbins = 14;
// static const double centbins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100};

// static const int ncentbins = 4;
// static const int cminCENT[] = {0,  5, 10, 70};
// static const int cmaxCENT[] = {5, 10, 70, 100};
// static const int NCbins = 4;
// static const double centbins[] = {0, 5, 10, 70, 100};

static const int ncentbins = 4;
static const int cminCENT[] = {0,  5, 40, 80};
static const int cmaxCENT[] = {5, 40, 80, 100};
static const int NCbins = 4;
static const double centbins[] = {0, 5, 10, 70, 100};
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
TH2D * multvsb;

TH1D * ptx;
TH1D * pty;
TH1D * ptxsum;
TH1D * ptysum;
TH2D * ptxysum;

TH1D * hcent;
double ccutlow[NCbins];
TH2D * v1true2D[NCbins];
TH2D * v2true2D[NCbins];
TH2D * qcnt[NCbins];

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
    multvsb = new TH2D("multvsb", "", bIN->GetNbinsX(), 0, 24, phiIN->GetNbinsX(), 0, 2e4);
    multvsb->SetOption("colz");
    for (int cbin = 0; cbin<ncentbins; cbin++) {
        v1true2D[cbin] = new TH2D(Form("v1true_%d_%d",cminCENT[cbin],cmaxCENT[cbin]), "", nptbins, ptbins, netabins, etabins);
        v1true2D[cbin]->SetXTitle("p_{T} (GeV/c)");
        v1true2D[cbin]->SetYTitle(Form("#eta (%d-%d%%)",cminCENT[cbin],cmaxCENT[cbin]));
        v1true2D[cbin]->SetOption("colz");
        v2true2D[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("v2true_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
        qcnt[cbin] = (TH2D *) v1true2D[cbin]->Clone(Form("qcnt_%d_%d",cminCENT[cbin],cmaxCENT[cbin]));
    }
    ptx = new TH1D("ptx", "", 100, -6, 6);
    pty = new TH1D("pty", "", 100, -6, 6);
    ptxsum = new TH1D("ptxsum", "", 100, -24, 24);
    ptysum = new TH1D("ptysum", "", 100, -24, 24);
    ptxysum = new TH2D("ptxysum", "", 50, -24, 24, 50, -24, 24);
    ptxysum->SetOption("colz");

    cout << "Retrieving centrality values... " << endl;
    // fcent = new TFile("hists/Cent.root","read");
    fcent = new TFile("hists/Cent_5_40_80.root","read");
    hcent = (TH1D *) fcent->Get("lowEdge");
    for (int i = 0; i<hcent->GetNbinsX(); i++) {
        ccutlow[i] = hcent->GetBinContent(i+1);
    }

    // fin = new TFile("../AMPTsample.root");
    // cout << "Reading file: ../AMPTsample.root" << endl;
    fin = new TFile("/rfs/wmcbrayer/AMPT/ampt_string_melting.root");
    cout << "Reading file: /rfs/wmcbrayer/AMPT/ampt_string_melting.root" << endl;
    tree0 = (TTree *) fin->Get("QWTreeMaker/trV");
    tree0->SetMakeClass(1);
    tree1 = (TTree *) fin->Get("QWHepMCMaker/trV");

    // int nevents = tree1->GetEntries();
    int nevents = 1e5;

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
    int nextStatus = 5;
    double tottime = 0;
    int ievnt = 0;
    TStopwatch * sw = new TStopwatch();
    sw->Start();
    cout << nevents << " events to be processed " << endl;
    cout << "Entering primary event loop..." << endl;
    while ( tree0->GetEntry(ievnt++) ) {
        if (ievnt>=nevents) break;
        if (fmod(double(ievnt+1), nevents/20.)==0) {
            cout << " " << nextStatus;
            nextStatus+=5;
            sw->Continue();
            double elapse0 = sw->RealTime();
            if (nextStatus == 10) tottime = elapse0;
            cout << "\tElapse time: " << Form("%3.2f",elapse0) << " seconds";
            cout << "\tEstimated total run time: " << Form("%3.2f",tottime*20./60./60.) << " hours" << endl;
        }

        bIN->Fill( b );
        epIN->Fill( bounds(1, PsiRP) );
        npartIN->Fill( Npart );
        ncollIN->Fill( Ncoll );
        multvsb->Fill( b, phi->size() );
        int cbin = hcent->GetXaxis()->FindBin(b)-1;
        if (cbin>=NCbins) {continue;}
        // cout<<"b: "<<b<<"\tcbin: "<<cbin<<endl;
        double ptxsum_ = 0;
        double ptysum_ = 0;
        for ( unsigned int i = 0; i<phi->size(); i++ ) {
            double phi_ = bounds(1, (*phi)[i]);
            double eta_ = (*eta)[i];
            double pt_  = (*pt)[i];
            phiIN->Fill( phi_ );
            etaIN->Fill( eta_ );
            ptIN->Fill( pt_ );
            ptx->Fill( pt_*TMath::Cos(phi_) );
            pty->Fill( pt_*TMath::Sin(phi_) );
            ptxsum_+=pt_*TMath::Cos(phi_);
            ptysum_+=pt_*TMath::Sin(phi_);

            if (eta_<=-2.4 || eta_>2.4) continue;
            int ebin = v1true2D[0]->GetYaxis()->FindBin(eta_)-1;
            int pbin = v1true2D[0]->GetXaxis()->FindBin(pt_)-1;
            if (ebin>v1true2D[0]->GetNbinsY() || pbin>v1true2D[0]->GetNbinsX()) continue;
            c1[cbin][pbin][ebin] += TMath::Cos(phi_ - PsiRP);
            c12[cbin][pbin][ebin] += pow(TMath::Cos(phi_ - PsiRP),2);
            c2[cbin][pbin][ebin] += TMath::Cos(2*(phi_ - PsiRP));
            c22[cbin][pbin][ebin] += pow(TMath::Cos(2*(phi_ - PsiRP)),2);
            cnt[cbin][pbin][ebin] += 1.;
        }
        ptxsum->Fill(ptxsum_);
        ptysum->Fill(ptysum_);
        ptxysum->Fill(ptxsum_, ptysum_);
        ptxsum_ = 0;
        ptysum_ = 0;
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
                qcnt[cbin]->SetBinContent(pbin+1, ebin+1, mult);
            }
        }
    }

    fout = new TFile("hists/amptVN.root","recreate");
    // fout = new TFile("hists/amptVN_5_40_80.root","recreate");
    fout->cd();
    phiIN->Write();
    etaIN->Write();
    ptIN->Write();
    bIN->Write();
    epIN->Write();
    npartIN->Write();
    ncollIN->Write();
    multvsb->Write();
    hcent->Write();
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TDirectory * tdcent = (TDirectory *) fout->mkdir(Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]));
        tdcent->cd();
        v1true2D[cbin]->Write();
        v2true2D[cbin]->Write();
        qcnt[cbin]->Write();
    }
    fout->cd();
    ptx->Write();
    pty->Write();
    ptxsum->Write();
    ptysum->Write();
    ptxysum->Write();

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
    multvsb->SetXTitle("b");
    multvsb->SetYTitle("Multiplicity");
    multvsb->Draw();
    cinputs->Print("figures/AMPT_inputs.png","png");
    cinputs->Write();


    TCanvas * cpt = new TCanvas("cpt", "cpt", 650, 600);
    cpt->Divide(2,2);
    cpt->cd(1);
    ptx->SetXTitle("p_{T}cos(#phi) (GeV/c)");
    ptx->Draw();
    cpt->cd(2);
    pty->SetXTitle("p_{T}sin(#phi) (GeV/c)");
    pty->Draw();
    TPad * padpt3 = (TPad *) cpt->cd(3);
    padpt3->SetLogy();
    ptIN->Draw();
    cpt->cd(4);
    TPaveText * txpt4 = new TPaveText(0.11, 0.29, 0.51, 0.81, "NDC");
    SetTPaveTxt(txpt4, 20);
    txpt4->AddText(Form("Events: %d",nevents));
    txpt4->AddText(Form("<p_{T}cos(#phi)>: %1.4f #pm %1.4f",ptx->GetMean(),ptx->GetMeanError()));
    txpt4->AddText(Form("<p_{T}sin(#phi)>: %1.4f #pm %1.4f",pty->GetMean(),pty->GetMeanError()));
    txpt4->Draw();
    cpt->Write();


    TCanvas * cptsum = new TCanvas("cptsum", "cptsum", 650, 600);
    cptsum->Divide(2,2);
    cptsum->cd(1);
    ptxsum->SetXTitle("#Sigmap_{T}cos(#phi) (GeV/c) per event");
    ptxsum->Draw();
    cptsum->cd(2);
    ptysum->SetXTitle("#Sigmap_{T}sin(#phi) (GeV/c) per event");
    ptysum->Draw();
    cptsum->cd(3);
    ptxysum->SetXTitle("#Sigmap_{T}cos(#phi) per event");
    ptxysum->SetYTitle("#Sigmap_{T}sin(#phi) per event");
    ptxysum->Draw();
    cptsum->cd(4);
    TPaveText * txptsum4 = new TPaveText(0.11, 0.29, 0.51, 0.81, "NDC");
    SetTPaveTxt(txptsum4, 20);
    txptsum4->AddText(Form("Events: %d",nevents));
    txptsum4->AddText(Form("#Sigmap_{T}cos(#phi): %1.4f #pm %1.4f",ptxsum->GetMean(),ptxsum->GetMeanError()));
    txptsum4->AddText(Form("#Sigmap_{T}sin(#phi): %1.4f #pm %1.4f",ptysum->GetMean(),ptysum->GetMeanError()));
    txptsum4->Draw();
    cptsum->Write();

    fout->Close();

}
