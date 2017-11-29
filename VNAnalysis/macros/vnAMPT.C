# include "TFile.h"
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

using namespace std;

static const int nptbins = 18;
static const double ptbins[] = {0.30,  0.40,  0.50,  0.60,  0.80,  1.00,  1.25,  1.50,  2.00,  2.50,  3.00,
                     3.50,  4.00,  5.00,  6.00,  7.00,  8.00,  10.00,  12.00};
static const int netabins = 12;
static const double etabins[] = {-2.4, -2.0, -1.6, -1.2, -0.8, -0.4,  0.0,
                     0.4,  0.8,  1.2,  1.6, 2.0,  2.4};
static const int ncentbins = 11;
static const int centBins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70};
static const double centRefBins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70};
static const int ncbins = 14;
static const int cmin[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 30,  50};
static const int cmax[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 30, 50, 100};

//-- MC inputs
TH1D * phiInput;
TH1D * etaInput;
TH1D * ptInput;
TH1D * binput;
TH1D * epInput;
TH1D * npartInput;
TH1D * ncollInput;

TFile * tfin;
TTree * tree0;
TTree * tree1;

TLeaf * Lphi;
TLeaf * Leta;
TLeaf * Lpt;
TLeaf * Lb;
TLeaf * Lep;
TLeaf * Lnpart;
TLeaf * Lncoll;

void ReadTree( int ievent );

void vnAMPT()
{

    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    tfin = new TFile("../AMPTsample.root");

    tree0 = (TTree *) tfin->Get("QWTreeMaker/trV");
    tree1 = (TTree *) tfin->Get("QWHepMCMaker/trV");
    tree0->AddFriend(tree1);

    phiInput   = new TH1D("phiInput", "", 50, -3.5, 3.5);
    etaInput   = new TH1D("etaInput", "", 50, -5.5, 5.5);
    ptInput    = new TH1D("ptInput", "", 50, 0, 12);
    binput     = new TH1D("binput", "", 50, 0, 30);
    epInput    = new TH1D("epInput", "", 50, -3.5, 3.5);
    npartInput = new TH1D("npartInput", "", 50, 0, 420);
    ncollInput = new TH1D("ncollInput", "", 50, 0, 3000);

    int nevents = tree0->GetEntries();
    int nextStatus = nevents/10;

    // main event loop
    for (Int_t ievent = 0; ievent<nevents; ievent++) {
        if (ievent>nextStatus) {
            cout << " " << nextStatus/(double)nevents << endl;
            nextStatus += nevents/10;
        }
        tree0->GetEntry( ievent );
        ReadTree( ievent );

    }

    phiInput->Draw();

}

void ReadTree( int ievent ) {

    Lphi   = (TLeaf *) tree0->GetLeaf("phi");
    Leta   = (TLeaf *) tree0->GetLeaf("eta");
    Lpt    = (TLeaf *) tree0->GetLeaf("pt");
    Lb     = (TLeaf *) tree0->GetLeaf("b");
    Lep    = (TLeaf *) tree0->GetLeaf("EP");
    Lnpart = (TLeaf *) tree0->GetLeaf("Npart");
    Lncoll = (TLeaf *) tree0->GetLeaf("Ncoll");

    phiInput->Fill(Lphi->GetValue());
    // etaInput   = new TH1D("etaInput", "", 50, -5.5, 5.5);
    // ptInput    = new TH1D("ptInput", "", 50, 0, 12);
    // binput     = new TH1D("binput", "", 50, 0, 30);
    // epInput    = new TH1D("epInput", "", 50, -3.5, 3.5);
    // npartInput = new TH1D("npartInput", "", 50, 0, 420);
    // ncollInput = new TH1D("ncollInput", "", 50, 0, 3000);
    //
    // Lphi;
    // Leta;
    // Lpt;
    // Lb;
    // Lep;
    // Lnpart;
    // Lncoll;

}
