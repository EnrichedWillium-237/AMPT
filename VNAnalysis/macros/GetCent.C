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
double b;
double PsiRP;
double Npart;
double Ncoll;
//----------------------------------

//-- MC inputs
TH1D * bIN;
TH1D * npartIN;
TH1D * ncollIN;

TH1D * hcent;
TH1D * h0;

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

    bIN     = new TH1D("bIN",     "", 200, 0, 24);
    npartIN = new TH1D("npartIN", "", 100, 0, 450);
    ncollIN = new TH1D("ncollIN", "", 100, 0, 2000);
    bIN->SetXTitle("b (fm)");

    fin = new TFile("../AMPTsample.root");
    cout << "Reading file: ../AMPTsample.root" << endl;
    tree0 = (TTree *) fin->Get("QWTreeMaker/trV");
    tree0->SetMakeClass(1);
    tree1 = (TTree *) fin->Get("QWHepMCMaker/trV");
    tree1->SetMakeClass(1);
    tree0->AddFriend(tree1);

    tree0->SetBranchAddress("b",      &b);
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
        npartIN->Fill( Npart );
        ncollIN->Fill( Ncoll );
    }

    // calculate percent centrality from impact parameter

    double bminCent[NCbins] = {0};
    double totInt = bIN->Integral(0,200);
    double bmin = 0;
    double bmax = 0.12;
    int cbin = 0;
    while (bmax < 24) {
        if (bmax>=24) continue;
        double binlow = bIN->FindBin(bmin+0.001);
        double binhigh = bIN->FindBin(bmax-0.001);
        double percntInt = 0.01*(double)(centbins[cbin+1]-centbins[cbin])*totInt;
        double subInt = bIN->Integral(binlow,binhigh);
        double subPerInt = 100*subInt/totInt;
        //cout<<"b: "<<bmin<<" - "<<bmax<<"\tbinlow: "<<binlow<<"\tbinhigh: "<<binhigh<<"\tsubInt: "<<subInt<<"\tsubPerInt: "<<subPerInt<<"\tpercntInt: "<<percntInt<<"\tcent: "<<centbins[cbin]<<" - "<<centbins[cbin+1]<<endl;
        if (subPerInt>((double)centbins[cbin+1]-centbins[cbin])) {
            bminCent[cbin] = bmin;
            bmin = bmax+0.001;
            cbin++;
        }
        bmax+=0.12-0.001;
    }
    hcent = new TH1D("centbins", "centbins", ncentbins, centbins);
    for (int i = 0; i<ncentbins; i++) {
        hcent->SetBinContent(i+1, bminCent[i]);
        hcent->SetBinError(i+1, 0.12);
    }
    hcent->SetTitle("");
    hcent->SetStats(0);
    hcent->SetYTitle("Minimum b (fm)");
    hcent->SetXTitle("Centrality (%)");
    hcent->GetYaxis()->SetRangeUser(0, 18);

    h0 = new TH1D("lowEdge", "lowEdge", NCbins, bminCent);
    for (int i = 0; i<h0->GetNbinsX(); i++) {
        h0->SetBinContent(i+1, centbins[i]);
        h0->SetBinError(i+1, 0.5);
    }
    h0->SetXTitle("Minimum b (fm)");
    h0->SetYTitle("Centrality (%)");


    TCanvas * c0 = new TCanvas("c0","c0",600,550);
    c0->cd();
    bIN->Draw();

    TCanvas * c1 = new TCanvas("c1","c1",600,550);
    c1->cd();
    hcent->Draw();

    TCanvas * c2 = new TCanvas("c2","c2",600,550);
    h0->Draw();

    if (!fopen("hists","r")) system("mkdir hists");

    fout = new TFile("hists/Cent.root","recreate");
    fout->cd();
    bIN->Write();
    hcent->Write();
    h0->Write();
    fout->Close();

}
