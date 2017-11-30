# include "TCanvas.h"
# include "TFile.h"
# include "TH1.h"
# include "TH2.h"
# include "TLeaf.h"
# include "TMath.h"
# include "TPad.h"
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
//--                            HF- track- track+ HF+ other
static const double emin[] = {-5.0, -0.5,  0.0,  3.0, -6.0};
static const double emax[] = {-3.0,  0.0,  0.5,  5.0,  6.0};
static const double pmin[] = { 0.3,  0.3,  0.3,  0.3,  0.0};
static const double pmax[] = {12.0,  3.0,  3.0, 12.0, 12.0};
static const int numEP = 5;
const string EPName[] = {"HFm", "trackm", "trackp", "HFp", "other"};
const string sideName[] = {"neg", "pos"};

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
TH1D * phiInput;
TH1D * etaInput;
TH1D * ptInput;
TH1D * binput;
TH1D * epInput;
TH1D * npartInput;
TH1D * ncollInput;
TH2D * sizevsb;

TH1D * phiPsi1[numEP];
TH1D * phiPsi2[numEP];
TH1D * phiPsi3[numEP];
TH1D * Psi1Psi[numEP];
TH1D * Psi2Psi[numEP];
TH1D * Psi3Psi[numEP];

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

# include "style.h"

Double_t bounds(int ord, double ang) {
    while (ang >  TMath::Pi()/ord) ang-=TMath::TwoPi()/ord;
    while (ang < -TMath::Pi()/ord) ang+=TMath::TwoPi()/ord;
    return ang;
}

typedef complex<double> comp;
comp zero (0,0);

void ReadTree( bool etaweights, bool ptweights )
{

    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    tfin = new TFile("../AMPTsample.root");

    cout << "Reading file: ../AMPTsample.root" << endl;
    if (etaweights) cout << "Calculating v1 using eta-dependent weighting" << endl;
    if (ptweights) cout << "Calculating v1 using pT-dependent weighting" << endl;

    tree0 = (TTree *) tfin->Get("QWTreeMaker/trV");
    tree1 = (TTree *) tfin->Get("QWHepMCMaker/trV");
    tree0->SetMakeClass(1);
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

    phiInput   = new TH1D("phiInput",   "", 100, -3.5, 3.5);
    etaInput   = new TH1D("etaInput",   "", 100, -6, 6);
    ptInput    = new TH1D("ptInput",    "", 100, 0, 12);
    binput     = new TH1D("binput",     "", 100, 0, 30);
    epInput    = new TH1D("epInput",    "", 100, -3.5, 3.5);
    npartInput = new TH1D("npartInput", "", 100, 0, 450);
    ncollInput = new TH1D("ncollInput", "", 100, 0, 2000);
    sizevsb    = new TH2D("sizevsb",    "", binput->GetNbinsX(), 0, 30, phiInput->GetNbinsX(), 0, 2e4);
    sizevsb->SetOption("colz");
    for (int nep = 0; nep<numEP; nep++) {
        phiPsi1[nep] = new TH1D(Form("phiPsi%s1",EPName[nep].data()), "", 100, -6, 6);
        phiPsi2[nep] = new TH1D(Form("phiPsi%s2",EPName[nep].data()), "", 100, -3, 3);
        phiPsi3[nep] = new TH1D(Form("phiPsi%s3",EPName[nep].data()), "", 100, -1.5, 1.5);
        Psi1Psi[nep] = new TH1D(Form("Psi%s1Psi",EPName[nep].data()), "", 100, -6, 6);
        Psi2Psi[nep] = new TH1D(Form("Psi%s2Psi",EPName[nep].data()), "", 100, -3, 3);
        Psi3Psi[nep] = new TH1D(Form("Psi%s3Psi",EPName[nep].data()), "", 100, -1.5, 1.5);
    }

    Double_t q1x[numEP];
    Double_t q1y[numEP];
    Double_t q2x[numEP];
    Double_t q2y[numEP];
    Double_t q3x[numEP];
    Double_t q3y[numEP];
    Double_t qcnt[numEP];

    Double_t Psi1[numEP];
    Double_t Psi2[numEP];
    Double_t Psi3[numEP];
    Double_t subcnt[numEP];

    comp Q1nA[2];
    comp Q1AB[2];
    comp Q1AC[2];
    comp Q1BC[2];
    comp Q2nA[2];
    comp Q2AB[2];
    comp Q2AC[2];
    comp Q2BC[2];

    double w1nA[2];
    double w1AB[2];
    double w1AC[2];
    double w1BC[2];
    double w2nA[2];
    double w2AB[2];
    double w2AC[2];
    double w2BC[2];

    for (int nep = 0; nep<numEP; nep++) {
        subcnt[nep] = 0;
    }

    for (int iside = 0; iside<2; iside++) {
        Q1nA[iside] = zero;
        Q1AB[iside] = zero;
        Q1AC[iside] = zero;
        Q1BC[iside] = zero;
        Q2nA[iside] = zero;
        Q2AB[iside] = zero;
        Q2AC[iside] = zero;
        Q2BC[iside] = zero;

        w1nA[iside] = 0;
        w1AB[iside] = 0;
        w1AC[iside] = 0;
        w1BC[iside] = 0;
        w2nA[iside] = 0;
        w2AB[iside] = 0;
        w2AC[iside] = 0;
        w2BC[iside] = 0;
    }

    // main event loop
    int nevents = tree0->GetEntries();
    int nextStatus = nevents/10;
    int ievnt = 0;
    cout << "Entering primary event loop..." <<endl;
    while ( tree0->GetEntry(ievnt++) ) {
        binput->Fill( b );
        epInput->Fill( PsiRP );
        npartInput->Fill( Npart );
        ncollInput->Fill( Ncoll );
        sizevsb->Fill( b, phi->size() );

        for (int nep = 0; nep<numEP; nep++) {
            q1x[nep] = 0;
            q1y[nep] = 0;
            q2x[nep] = 0;
            q2y[nep] = 0;
            q3x[nep] = 0;
            q3y[nep] = 0;
            qcnt[nep] = 0;
            Psi1[nep] = 0;
            Psi2[nep] = 0;
            Psi3[nep] = 0;
        }

        for ( unsigned int i = 0; i<phi->size(); i++) {
            double phi_ = bounds(1, (*phi)[i]);
            double eta_ = (*eta)[i];
            double pt_  = (*pt)[i];
            phiInput->Fill( phi_ );
            etaInput->Fill( eta_ );
            ptInput->Fill( pt_ );
            for (int nep = 0; nep<numEP; nep++) {
                if ( eta_>=emin[nep] && eta_<emax[nep]) {
                    double w1 = 1;
                    double w2 = 1;
                    double w3 = 1;
                    if (etaweights && eta_<0) w1*=-1;
                    q1x[nep] += w1*TMath::Cos(phi_);
                    q1y[nep] += w1*TMath::Sin(phi_);
                    q2x[nep] += w2*TMath::Cos(2*phi_);
                    q2y[nep] += w2*TMath::Sin(2*phi_);
                    q3x[nep] += w3*TMath::Cos(3*phi_);
                    q3y[nep] += w3*TMath::Sin(3*phi_);
                    qcnt[nep]++;
                }
            }
        }
        for (int nep = 0; nep<numEP; nep++) {
            Psi1[nep] = TMath::ATan2(q1y[nep],q1x[nep]);
            Psi2[nep] = TMath::ATan2(q2y[nep],q2x[nep])/2.;
            Psi3[nep] = TMath::ATan2(q3y[nep],q3x[nep])/3.;

            Psi1Psi[nep]->Fill(bounds(1, Psi1[nep]/PsiRP));
            Psi2Psi[nep]->Fill(bounds(2, Psi2[nep]/PsiRP));
            Psi3Psi[nep]->Fill(bounds(3, Psi3[nep]/PsiRP));
        }

    }
}

void vnAMPT() {

    bool etaweights = true;
    bool ptweights = false;

    ReadTree( etaweights, ptweights );



    TCanvas * cinputs = new TCanvas("cinputs","cinputs",1200,600);
    cinputs->Divide(4,2);
    cinputs->cd(1);
    phiInput->SetXTitle("#phi");
    phiInput->Draw();
    cinputs->cd(2);
    etaInput->SetXTitle("#eta");
    etaInput->Draw();
    TPad * padinputs3 = (TPad *) cinputs->cd(3);
    padinputs3->SetLogy();
    ptInput->SetXTitle("p_{T} (GeV/c)");
    ptInput->Draw();
    cinputs->cd(4);
    binput->SetXTitle("b (fm)");
    binput->Draw();
    cinputs->cd(5);
    epInput->SetXTitle("#Psi_{RP}");
    epInput->Draw();
    cinputs->cd(6);
    npartInput->SetXTitle("N_{part}");
    npartInput->Draw();
    cinputs->cd(7);
    ncollInput->SetXTitle("N_{coll}");
    ncollInput->Draw();
    cinputs->cd(8);
    sizevsb->SetXTitle("b");
    sizevsb->SetYTitle("Multiplicity");
    sizevsb->Draw();


}
