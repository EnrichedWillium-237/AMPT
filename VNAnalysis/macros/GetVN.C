# include "TCanvas.h"
# include "TFile.h"
# include "TGraphErrors.h"
# include "TH1.h"
# include "TH2.h"
# include "TLeaf.h"
# include "TMath.h"
# include "TRandom3.h"
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

using namespace hi;

static const int nptbins = 18;
static const double ptbins[] = {0.30,  0.40,  0.50,  0.60,  0.80,  1.00,  1.25,  1.50,  2.00,  2.50,  3.00,
    3.50,  4.00,  5.00,  6.00,  7.00,  8.00,  10.00,  12.00};
static const int netabins = 12;
static const double etabins[] = {-2.4, -2.0, -1.6, -1.2, -0.8, -0.4,  0.0,  0.4,  0.8,  1.2,  1.6,  2.0,  2.4};
static const int ncentbins = 14;
static const double centbins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100};

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

TFile * fin;
TFile * fout;

TTree * tree0;
TTree * tree1;
TLeaf * lphi;
TLeaf * leta;
TLeaf * lpt;
TLeaf * lb;
TLeaf * lep;
TLeaf * lnpart;
TLeaf * lncoll;

# include "style.h"

Double_t bounds( int ord, double ang ) {
    while (ang >  TMath::Pi()/ord) ang-=TMath::TwoPi()/ord;
    while (ang < -TMath::Pi()/ord) ang+=TMath::TwoPi()/ord;
    return ang;
}

typedef complex<double> comp;
comp zero (0,0);

void GetVN()
{
    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    phiIN   = new TH1D("phiIN",   "", 100, -3.5, 3.5);
    etaIN   = new TH1D("etaIN",   "", 100, -6, 6);
    ptIN    = new TH1D("ptIN",    "", 100, 0, 12);
    bIN     = new TH1D("bIN",     "", 100, 0, 30);
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
    cout << "Entering primary event loop..." <<endl;
    while ( tree0->GetEntry(ievnt++) ) {
        if (fmod(double(ievnt+1), nevents/20.)==0) {
            cout << " " << nextStatus << endl;
            nextStatus+=5;
        }

        bIN->Fill( b );
        epIN->Fill( bounds(1, PsiRP) );
        npartIN->Fill( Npart );
        ncollIN->Fill( Ncoll );
        sizevsb->Fill( b, phi->size() );

        for ( unsigned int i = 0; i<phi->size(); i++ ) {
            double phi_ = bounds(1, (*phi)[i]);
            double eta_ = (*eta)[i];
            double pt_  = (*pt)[i];
            phiIN->Fill( phi_ );
            etaIN->Fill( eta_ );
            ptIN->Fill( pt_ );
        }
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


}
