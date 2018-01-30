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

# include "../HiEvtPlaneList.h"

static const int ncentbins = 13;
static const int cminCENT[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 20,  60};
static const int cmaxCENT[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 20, 60, 100};
string ctag[] = {"0_5", "5_10", "10_15", "15_20", "20_25", "25_30", "30_35", "35_40", "40_50", "50_60", "60_70", "0_20", "20_60"}
static const int nptbins = 18;
static const double ptbins[] = {0.30,  0.40,  0.50,  0.60,  0.80,  1.00,  1.25,  1.50,  2.00,  2.50,  3.00,
    3.50,  4.00,  5.00,  6.00,  7.00,  8.00,  10.00,  12.00};
static const int netabins = 12;
static const double etabins[] = {-2.4, -2.0, -1.6, -1.2, -0.8, -0.4,  0.0,  0.4,  0.8,  1.2,  1.6,  2.0,  2.4};

//----------------------------------
// Tree variables
//
vector<double> *phi = 0;
vector<double> *eta = 0;
vector<double> *pt = 0;
vector<double> *charge = 0;
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

TH1D * centbins;

TFile * fin;
TFile * fout;

TTree * tree0;
TTree * tree1;

# include "style.h"

Double_t bounds( int ord, double ang ) {
    while (ang >  TMath::Pi()/ord) ang-=TMath::TwoPi()/ord;
    while (ang < -TMath::Pi()/ord) ang+=TMath::TwoPi()/ord;
    return ang;
}

typedef complex<double> comp;
comp zero (0,0);

void GetCent()
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
    sizevsb = new TH2D("sizevsb", "", bIN->GetNbinsX(), 0, 30, phiIN->GetNbinsX(), 0, 2e4);
    sizevsb->SetOption("colz");

    fin = new TFile("../AMPTsample.root");
    cout << "Reading file: ../AMPTsample.root" << endl;
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

    // main event loop
    int nevents = tree0->GetEntries();
    int nextStatus = 5;
    int ievnt = 0;
    TStopwatch * sw0 = new TStopwatch();
    TStopwatch * sw1 = new TStopwatch();
    sw0->Start();
    cout << "Entering primary event loop..." <<endl;
    while ( tree0->GetEntry(ievnt++) ) {
        if (fmod(double(ievnt+1), nevents/20.)==0) {
            cout << " " << nextStatus;
            nextStatus+=5;

            sw1->Start();
            sw0->Continue();
            sw1->Continue();
            double elapse0 = sw0->RealTime();
            double elapse1 = sw1->RealTime();
            cout << "\tElapse time: " << Form("%3.2f",elapse0) << " seconds";
            cout << "\tEstimated total run time: " << Form("%3.2f",elapse1*20./60./60.) << " hours" << endl;
        }

        bIN->Fill( b );
        epIN->Fill( bounds(1, PsiRP) );
        npartIN->Fill( Npart );
        ncollIN->Fill( Ncoll );
        sizevsb->Fill( b, phi->size() );

    }

    // calculate percent centrality from impact parameter
    centbins = new TH1D("centbins","centbins",ncentbins,centbins);
    centbins->SetXTitle("Centrality (%%)");
    centbins->SetYTitle("Minimum b (fm)");

    double totInt = bIN->Integral(0,200);
    double bmin = 0;
    double bmax = 0.12;
    cout << "Total integral from 0 to 24 fm: " << totInt << endl;
    int cbin = 0;
    while (bmax < 24) {
        if (bmax>=24) continue;
        double binlow = bIN->FindBin(bmin+0.001);
        double binhigh = bIN->FindBin(bmax-0.001);
        double percntInt = 0.01*(double)(cmaxCENT[cbin]-cminCENT[cbin])*totInt;
        double subInt = bIN->Integral(binlow,binhigh);
        double subPerInt = 100*subInt/totInt;
        //cout<<"b: "<<bmin<<" - "<<bmax<<"\tbinlow: "<<binlow<<"\tbinhigh: "<<binhigh<<"\tsubInt: "<<subInt<<"\tsubPerInt: "<<subPerInt<<"\tpercntInt: "<<percntInt<<"\tcent: "<<cbin<<"\t"<<cminCENT[cbin]<<" - "<<cmaxCENT[cbin]<<endl;
        if (subPerInt>((double)cmaxCENT[cbin]-cminCENT[cbin])) {
            centbins->SetBinContent(cbin, bmin);
            centbins->SetBinError(cbin, 0.12);
            bmin = bmax+0.001;
            cbin++;
        }
        bmax+=0.12-0.001;
    }


    TCanvas * c0 = new TCanvas("c0","c0",600,550);
    c0->cd();
    bIN->Draw();

    TCanvas * c1 = new TCanvas("c1","c1",600,550);
    c1->cd();
    centbins->Draw();


    if (!fopen("hists","r")) system("mkdir hists");

    fout = new TFile("hists/Cent.root","recreate");
    fout->cd();
    bIN->Write();
    centbins->Write();
    fout->Close();

}
