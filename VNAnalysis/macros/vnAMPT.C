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
static const double centBins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70};
static const int ncbins = 14;
static const int cmin[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 30,  50};
static const int cmax[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 30, 50, 100};
static const double npartBins[] = {420, 355, 305, 260, 221, 186, 156, 132, 102, 67, 40, 23};
//--                            HF- track- track+ HF+ other
static const double emin[] = {-5.0, -0.5,  0.0,  3.0, -6.0};
static const double emax[] = {-3.0,  0.0,  0.5,  5.0,  6.0};
static const double pmin[] = { 0.3,  0.3,  0.3,  0.3,  0.0};
static const double pmax[] = {12.0,  3.0,  3.0, 12.0, 12.0};
static const int numEP = 5;
const string EPName[] = {"HFm", "trackm", "trackp", "HFp", "other"};
static const double eminPOI[] = {-2.4, 0.0};
static const double emaxPOI[] = { 0.0, 2.4};
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

TH1D * qA[ncentbins][11];
TH1D * qB[ncentbins][11];
TH1D * wnA[ncentbins][11];
TH1D * wnB[ncentbins][11];
TH1D * qABp[3][ncentbins][11];
TH1D * qACp[3][ncentbins][11];
TH1D * qBCp[3][ncentbins][11];
TH1D * qABm[3][ncentbins][11];
TH1D * qACm[3][ncentbins][11];
TH1D * qBCm[3][ncentbins][11];
TH1D * qABpcnt[3][ncentbins][11];
TH1D * qACpcnt[3][ncentbins][11];
TH1D * qBCpcnt[3][ncentbins][11];
TH1D * qABmcnt[3][ncentbins][11];
TH1D * qACmcnt[3][ncentbins][11];
TH1D * qBCmcnt[3][ncentbins][11];

TRandom3 * ran;
TFile * tfin;
TFile * tfout;
TTree * tree0;
TTree * tree1;
TLeaf * Lphi;
TLeaf * Leta;
TLeaf * Lpt;
TLeaf * Lb;
TLeaf * Lep;
TLeaf * Lnpart;
TLeaf * Lncoll;
TH1D * Npartbins;
TH1D * centbins;
int centval;

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

    ran = new TRandom3();

    Double_t n1x[netabins];
    Double_t n1y[netabins];
    Double_t n1cnt[netabins];
    Double_t q1x[numEP];
    Double_t q1y[numEP];
    Double_t q2x[numEP];
    Double_t q2y[numEP];
    Double_t q3x[numEP];
    Double_t q3y[numEP];
    Double_t q1cnt[numEP];
    Double_t q2cnt[numEP];
    Double_t q3cnt[numEP];

    Double_t Psi1[numEP];
    Double_t Psi2[numEP];
    Double_t Psi3[numEP];


    // main event loop
    int nevents = tree0->GetEntries();
    int nextStatus = 10;
    int ievnt = 0;
    cout << "Entering primary event loop..." <<endl;
    while ( tree0->GetEntry(ievnt++) ) {
        if (fmod(double(ievnt+1), nevents/10.)==0) {
            cout << " " << nextStatus << endl;
            nextStatus+=10;
        }

        binput->Fill( b );
        epInput->Fill( PsiRP );
        npartInput->Fill( Npart );
        ncollInput->Fill( Ncoll );
        sizevsb->Fill( b, phi->size() );

        int bin = -1;
        for (int j = 0; j<ncentbins; j++) {
            if (Npart>=npartBins[j+1] && Npart<npartBins[j]) {bin = j; centbins->Fill(centBins[bin]);}
        }
        centbins->SetMinimum(0);
        centval = bin;
        if (centval<0) continue;

        for (int nep = 0; nep<numEP; nep++) {
            q1x[nep] = 0;
            q1y[nep] = 0;
            q2x[nep] = 0;
            q2y[nep] = 0;
            q3x[nep] = 0;
            q3y[nep] = 0;
            q1cnt[nep] = 0;
            q2cnt[nep] = 0;
            q3cnt[nep] = 0;
            Psi1[nep] = 0;
            Psi2[nep] = 0;
            Psi3[nep] = 0;
        }
        for (int ebin = 0; ebin<netabins; ebin++) {
            n1x[ebin] = 0;
            n1y[ebin] = 0;
            n1cnt[ebin] = 0;
        }
        for ( unsigned int i = 0; i<phi->size(); i++ ) {
            double phi_ = bounds(1, (*phi)[i]);
            double eta_ = (*eta)[i];
            double pt_  = (*pt)[i];
            phiInput->Fill( phi_ );
            etaInput->Fill( eta_ );
            ptInput->Fill( pt_ );
            for (int ebin = 0; ebin<netabins; ebin++) {
                if (eta_<etabins[ebin] || eta_>etabins[ebin+1] || pt_<0.3 || pt_>3.0) continue;
                n1x[ebin] += TMath::Cos(phi_);
                n1y[ebin] += TMath::Sin(phi_);
                n1cnt[ebin]++;
                //cout<<ebin<<"\t"<<n1x[ebin]<<"\t"<<n1y[ebin]<<endl;
                //cout<<"ebin: "<<ebin<<"\t"<<etabins[ebin]<<"\t"<<etabins[ebin+1]<<"\teta:"<<eta_<<endl;
                // if (eta_>=etabins[ebin] && eta_<etabins[ebin+1] && pt_>=0.3 && pt_<3.0) {
                //     n1x[ebin] += TMath::Cos(phi_);
                //     n1y[ebin] += TMath::Sin(phi_);
                //     n1cnt[ebin]++;
                // }
            }
            for (int nep = 0; nep<numEP; nep++) {
                if ( eta_>=emin[nep] && eta_<emax[nep] && pt_>=pmin[nep] && pt_<pmax[nep] ) {
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
                    q1cnt[nep] += w1;
                    q2cnt[nep] += w2;
                    q3cnt[nep] += w3;
                }
            }
        }
        for (int nep = 0; nep<numEP; nep++) {
            Psi1[nep] = TMath::ATan2(q1y[nep],q1x[nep]);
            Psi2[nep] = TMath::ATan2(q2y[nep],q2x[nep])/2.;
            Psi3[nep] = TMath::ATan2(q3y[nep],q3x[nep])/3.;

            Psi1Psi[nep]->Fill(bounds(1, Psi1[nep] - PsiRP));
            Psi2Psi[nep]->Fill(bounds(2, Psi2[nep] - PsiRP));
            Psi3Psi[nep]->Fill(bounds(3, Psi3[nep] - PsiRP));
            for ( unsigned int i = 0; i<phi->size(); i++) {
                double phi_ = bounds(1, (*phi)[i]);
                phiPsi1[nep]->Fill(bounds(1, phi_ - Psi1[nep]));
                phiPsi2[nep]->Fill(bounds(2, phi_ - Psi2[nep]));
                phiPsi3[nep]->Fill(bounds(3, phi_ - Psi3[nep]));
            }
        }
        //-- calculate vn
        int HFm = 0;
        int trackm = 1;
        int trackp = 2;
        int HFp = 3;

        comp Q1Ap( q1x[HFp], q1y[HFp] );
        comp Q1Bp( q1x[HFm], q1y[HFm] );
        comp Q1Cp( q1x[trackp], q1y[trackp] );
        comp Q1Am( q1x[HFm], q1y[HFm] );
        comp Q1Bm( q1x[HFp], q1y[HFp] );
        comp Q1Cm( q1x[trackm], q1y[trackm] );

        comp Q2Ap( q2x[HFp], q2y[HFp] );
        comp Q2Bp( q2x[HFm], q2y[HFm] );
        comp Q2Cp( q2x[trackp], q2y[trackp] );
        comp Q2Am( q2x[HFm], q2y[HFm] );
        comp Q2Bm( q2x[HFp], q2y[HFp] );
        comp Q2Cm( q2x[trackm], q2y[trackm] );

        comp Q3Ap( q2x[HFp], q2y[HFp] );
        comp Q3Bp( q2x[HFm], q2y[HFm] );
        comp Q3Cp( q2x[trackp], q2y[trackp] );
        comp Q3Am( q2x[HFm], q2y[HFm] );
        comp Q3Bm( q2x[HFp], q2y[HFp] );
        comp Q3Cm( q2x[trackm], q2y[trackm] );

        comp AB1p = Q1Ap * conj(Q1Bp);
        comp AC1p = Q1Ap * conj(Q1Cp);
        comp BC1p = Q1Bp * conj(Q1Cp);
        comp AB1m = Q1Am * conj(Q1Bm);
        comp AC1m = Q1Am * conj(Q1Cm);
        comp BC1m = Q1Bm * conj(Q1Cm);

        comp AB2p = Q2Ap * conj(Q2Bp);
        comp AC2p = Q2Ap * conj(Q2Cp);
        comp BC2p = Q2Bp * conj(Q2Cp);
        comp AB2m = Q2Am * conj(Q2Bm);
        comp AC2m = Q2Am * conj(Q2Cm);
        comp BC2m = Q2Bm * conj(Q2Cm);

        comp AB3p = Q3Ap * conj(Q3Bp);
        comp AC3p = Q3Ap * conj(Q3Cp);
        comp BC3p = Q3Bp * conj(Q3Cp);
        comp AB3m = Q3Am * conj(Q3Bm);
        comp AC3m = Q3Am * conj(Q3Cm);
        comp BC3m = Q3Bm * conj(Q3Cm);

        qABp[0][centval][0]->Fill(0., AB1p.real());
        qACp[0][centval][0]->Fill(0., AC1p.real());
        qBCp[0][centval][0]->Fill(0., BC1p.real());
        qABm[0][centval][0]->Fill(0., AB1m.real());
        qACm[0][centval][0]->Fill(0., AC1m.real());
        qBCm[0][centval][0]->Fill(0., BC1m.real());

        qABp[1][centval][0]->Fill(0., AB1p.real());
        qACp[1][centval][0]->Fill(0., AC1p.real());
        qBCp[1][centval][0]->Fill(0., BC1p.real());
        qABm[1][centval][0]->Fill(0., AB1m.real());
        qACm[1][centval][0]->Fill(0., AC1m.real());
        qBCm[1][centval][0]->Fill(0., BC1m.real());

        qABp[2][centval][0]->Fill(0., AB1p.real());
        qACp[2][centval][0]->Fill(0., AC1p.real());
        qBCp[2][centval][0]->Fill(0., BC1p.real());
        qABm[2][centval][0]->Fill(0., AB1m.real());
        qACm[2][centval][0]->Fill(0., AC1m.real());
        qBCm[2][centval][0]->Fill(0., BC1m.real());

        qABpcnt[0][centval][0]->Fill(0., q1cnt[HFp]*q1cnt[HFm]);
        qACpcnt[0][centval][0]->Fill(0., q1cnt[HFp]*q1cnt[trackp]);
        qBCpcnt[0][centval][0]->Fill(0., q1cnt[HFm]*q1cnt[trackp]);
        qABmcnt[0][centval][0]->Fill(0., q1cnt[HFm]*q1cnt[HFp]);
        qACmcnt[0][centval][0]->Fill(0., q1cnt[HFm]*q1cnt[trackm]);
        qBCmcnt[0][centval][0]->Fill(0., q1cnt[HFp]*q1cnt[trackm]);

        qABpcnt[1][centval][0]->Fill(0., q2cnt[HFp]*q2cnt[HFm]);
        qACpcnt[1][centval][0]->Fill(0., q2cnt[HFp]*q2cnt[trackp]);
        qBCpcnt[1][centval][0]->Fill(0., q2cnt[HFm]*q2cnt[trackp]);
        qABmcnt[1][centval][0]->Fill(0., q2cnt[HFm]*q2cnt[HFp]);
        qACmcnt[1][centval][0]->Fill(0., q2cnt[HFm]*q2cnt[trackm]);
        qBCmcnt[1][centval][0]->Fill(0., q2cnt[HFp]*q2cnt[trackm]);

        qABpcnt[2][centval][0]->Fill(0., q3cnt[HFp]*q3cnt[HFm]);
        qACpcnt[2][centval][0]->Fill(0., q3cnt[HFp]*q3cnt[trackp]);
        qBCpcnt[2][centval][0]->Fill(0., q3cnt[HFm]*q3cnt[trackp]);
        qABmcnt[2][centval][0]->Fill(0., q3cnt[HFm]*q3cnt[HFp]);
        qACmcnt[2][centval][0]->Fill(0., q3cnt[HFm]*q3cnt[trackm]);
        qBCmcnt[2][centval][0]->Fill(0., q3cnt[HFp]*q3cnt[trackm]);

        for (int ebin = 0; ebin<netabins; ebin++) {
            comp Qn1( n1x[ebin], n1y[ebin] );
            comp nA1 = Qn1 * conj(Q1Ap);
            comp nB1 = Qn1 * conj(Q1Am);
            //qA[centval][0]->Fill(ebin, nA1.real());
            qA[centval][0]->SetBinContent(ebin+1, qA[centval][0]->GetBinContent(ebin+1) + nA1.real());
            //qB[centval][0]->Fill(ebin, nB1.real());
            qB[centval][0]->SetBinContent(ebin+1, qB[centval][0]->GetBinContent(ebin+1) + nB1.real());
            //wnA[centval][0]->Fill(ebin, n1cnt[ebin]*q1cnt[HFp]);
            wnA[centval][0]->SetBinContent(ebin+1, wnA[centval][0]->GetBinContent(ebin+1) + n1cnt[ebin]*q1cnt[HFp]);
            //wnB[centval][0]->Fill(ebin, n1cnt[ebin]*q1cnt[HFm]);
            wnB[centval][0]->SetBinContent(ebin+1, wnB[centval][0]->GetBinContent(ebin+1) + n1cnt[ebin]*q1cnt[HFp]);

        }

        int k = (int)(ran->Uniform(0,9.999))+1;
        qABp[0][centval][k]->Fill(0., AB1p.real());
        qACp[0][centval][k]->Fill(0., AC1p.real());
        qBCp[0][centval][k]->Fill(0., BC1p.real());
        qABm[0][centval][k]->Fill(0., AB1m.real());
        qACm[0][centval][k]->Fill(0., AC1m.real());
        qBCm[0][centval][k]->Fill(0., BC1m.real());

        qABp[1][centval][k]->Fill(0., AB2p.real());
        qACp[1][centval][k]->Fill(0., AC2p.real());
        qBCp[1][centval][k]->Fill(0., BC2p.real());
        qABm[1][centval][k]->Fill(0., AB2m.real());
        qACm[1][centval][k]->Fill(0., AC2m.real());
        qBCm[1][centval][k]->Fill(0., BC2m.real());

        qABp[2][centval][k]->Fill(0., AB1p.real());
        qACp[2][centval][k]->Fill(0., AC1p.real());
        qBCp[2][centval][k]->Fill(0., BC1p.real());
        qABm[2][centval][k]->Fill(0., AB1m.real());
        qACm[2][centval][k]->Fill(0., AC1m.real());
        qBCm[2][centval][k]->Fill(0., BC1m.real());

        qABpcnt[0][centval][k]->Fill(0., q1cnt[HFp]*q1cnt[HFm]);
        qACpcnt[0][centval][k]->Fill(0., q1cnt[HFp]*q1cnt[trackp]);
        qBCpcnt[0][centval][k]->Fill(0., q1cnt[HFm]*q1cnt[trackp]);
        qABmcnt[0][centval][k]->Fill(0., q1cnt[HFm]*q1cnt[HFp]);
        qACmcnt[0][centval][k]->Fill(0., q1cnt[HFm]*q1cnt[trackm]);
        qBCmcnt[0][centval][k]->Fill(0., q1cnt[HFp]*q1cnt[trackm]);

        qABpcnt[1][centval][k]->Fill(0., q2cnt[HFp]*q2cnt[HFm]);
        qACpcnt[1][centval][k]->Fill(0., q2cnt[HFp]*q2cnt[trackp]);
        qBCpcnt[1][centval][k]->Fill(0., q2cnt[HFm]*q2cnt[trackp]);
        qABmcnt[1][centval][k]->Fill(0., q2cnt[HFm]*q2cnt[HFp]);
        qACmcnt[1][centval][k]->Fill(0., q2cnt[HFm]*q2cnt[trackm]);
        qBCmcnt[1][centval][k]->Fill(0., q2cnt[HFp]*q2cnt[trackm]);

        qABpcnt[2][centval][k]->Fill(0., q3cnt[HFp]*q3cnt[HFm]);
        qACpcnt[2][centval][k]->Fill(0., q3cnt[HFp]*q3cnt[trackp]);
        qBCpcnt[2][centval][k]->Fill(0., q3cnt[HFm]*q3cnt[trackp]);
        qABmcnt[2][centval][k]->Fill(0., q3cnt[HFm]*q3cnt[HFp]);
        qACmcnt[2][centval][k]->Fill(0., q3cnt[HFm]*q3cnt[trackm]);
        qBCmcnt[2][centval][k]->Fill(0., q3cnt[HFp]*q3cnt[trackm]);

        for (int ebin = 0; ebin<netabins; ebin++) {
            comp Qn1( n1x[ebin], n1y[ebin] );
            comp nA1 = Qn1 * conj(Q1Ap);
            comp nB1 = Qn1 * conj(Q1Am);
            //qA[centval][k]->Fill(ebin, nA1.real());
            qA[centval][k]->SetBinContent(ebin+1, qA[centval][k]->GetBinContent(ebin+1) + nA1.real());
            //qB[centval][k]->Fill(ebin, nB1.real());
            qB[centval][k]->SetBinContent(ebin+1, qB[centval][k]->GetBinContent(ebin+1) + nB1.real());
            //wnA[centval][k]->Fill(ebin, n1cnt[ebin]*q1cnt[HFp]);
            wnA[centval][k]->SetBinContent(ebin+1, wnA[centval][k]->GetBinContent(ebin+1) + n1cnt[ebin]*q1cnt[HFp]);
            //wnB[centval][k]->Fill(ebin, n1cnt[ebin]*q1cnt[HFm]);
            wnB[centval][k]->SetBinContent(ebin+1, wnB[centval][k]->GetBinContent(ebin+1) + n1cnt[ebin]*q1cnt[HFp]);
        }
    }

    string ntag = "";
    if (etaweights) ntag+="_eta_weights";
    if (ptweights) ntag+="_pt_weights";
    tfout = new TFile(Form("AMPTvn%s.root",ntag.data()),"recreate");
    for (int cbin = 0; cbin<ncentbins; cbin++) {
        TDirectory * tdcent = (TDirectory *) tfout->mkdir(Form("%d_%d",cmin[cbin],cmax[cbin]));
        tdcent->cd();
        qA[cbin][0]->Write();
        qB[cbin][0]->Write();
        wnA[cbin][0]->Write();
        wnB[cbin][0]->Write();
        for (int ord = 0; ord<3; ord++) {
            qABp[ord][cbin][0]->Write();
            qACp[ord][cbin][0]->Write();
            qBCp[ord][cbin][0]->Write();
            qABm[ord][cbin][0]->Write();
            qACm[ord][cbin][0]->Write();
            qBCm[ord][cbin][0]->Write();
            qABpcnt[ord][cbin][0]->Write();
            qACpcnt[ord][cbin][0]->Write();
            qBCpcnt[ord][cbin][0]->Write();
            qABmcnt[ord][cbin][0]->Write();
            qACmcnt[ord][cbin][0]->Write();
            qBCmcnt[ord][cbin][0]->Write();
        }

        TDirectory * tderr = (TDirectory *) tdcent->mkdir("SubEvents");
        tderr->cd();
        for (int k = 1; k<=10; k++) {
            qA[cbin][k]->Write();
            qB[cbin][k]->Write();
            wnA[cbin][k]->Write();
            wnB[cbin][k]->Write();
            for (int ord = 0; ord<3; ord++) {
                qABp[ord][cbin][k]->Write();
                qACp[ord][cbin][k]->Write();
                qBCp[ord][cbin][k]->Write();
                qABm[ord][cbin][k]->Write();
                qACm[ord][cbin][k]->Write();
                qBCm[ord][cbin][k]->Write();
                qABpcnt[ord][cbin][k]->Write();
                qACpcnt[ord][cbin][k]->Write();
                qBCpcnt[ord][cbin][k]->Write();
                qABmcnt[ord][cbin][k]->Write();
                qACmcnt[ord][cbin][k]->Write();
                qBCmcnt[ord][cbin][k]->Write();
            }
        }
    }
    //tfout->Close();

}


void vnAMPT() {

    bool etaweights = true;
    bool ptweights = false;

    double npartBins_[] = {23, 40, 67, 102, 132, 156, 186, 221, 260, 305, 355, 420};
    Npartbins = new TH1D("Npartbins", "", ncentbins, npartBins_);
    centbins = new TH1D("centbins", "", ncentbins, centBins);
    for (int cbin = 0; cbin<ncentbins; cbin++) {
        qA[cbin][0] = new TH1D(Form("qA_%d_%d",cmin[cbin],cmax[cbin]), "", netabins, etabins);
        qB[cbin][0] = new TH1D(Form("qB_%d_%d",cmin[cbin],cmax[cbin]), "", netabins, etabins);
        wnA[cbin][0] = new TH1D(Form("wnA_%d_%d",cmin[cbin],cmax[cbin]), "", netabins, etabins);
        wnB[cbin][0] = new TH1D(Form("wnB_%d_%d",cmin[cbin],cmax[cbin]), "", netabins, etabins);
        for (int ord = 1; ord<=3; ord++) {
            qABp[ord-1][cbin][0] = new TH1D(Form("qABp%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qABp[ord-1][cbin][0]->SetDirectory(0);
            qACp[ord-1][cbin][0] = new TH1D(Form("qACp%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qACp[ord-1][cbin][0]->SetDirectory(0);
            qBCp[ord-1][cbin][0] = new TH1D(Form("qBCp%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qBCp[ord-1][cbin][0]->SetDirectory(0);
            qABm[ord-1][cbin][0] = new TH1D(Form("qABm%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qABm[ord-1][cbin][0]->SetDirectory(0);
            qACm[ord-1][cbin][0] = new TH1D(Form("qACm%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qACm[ord-1][cbin][0]->SetDirectory(0);
            qBCm[ord-1][cbin][0] = new TH1D(Form("qBCm%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qBCm[ord-1][cbin][0]->SetDirectory(0);
            qABpcnt[ord-1][cbin][0] = new TH1D(Form("qABpcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qABpcnt[ord-1][cbin][0]->SetDirectory(0);
            qACpcnt[ord-1][cbin][0] = new TH1D(Form("qACpcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qACpcnt[ord-1][cbin][0]->SetDirectory(0);
            qBCpcnt[ord-1][cbin][0] = new TH1D(Form("qBCpcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qBCpcnt[ord-1][cbin][0]->SetDirectory(0);
            qABmcnt[ord-1][cbin][0] = new TH1D(Form("qABmcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qABmcnt[ord-1][cbin][0]->SetDirectory(0);
            qACmcnt[ord-1][cbin][0] = new TH1D(Form("qACmcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qACmcnt[ord-1][cbin][0]->SetDirectory(0);
            qBCmcnt[ord-1][cbin][0] = new TH1D(Form("qBCmcnt%d_%d_%d",ord,cmin[cbin],cmax[cbin]), "", 1, 0, 1);
            qBCmcnt[ord-1][cbin][0]->SetDirectory(0);
        }
        for (int k = 1; k<=10; k++) {
            qA[cbin][k] = new TH1D(Form("qA_%d_%d_%d",cmin[cbin],cmax[cbin],k), "", netabins, etabins);
            qB[cbin][k] = new TH1D(Form("qB_%d_%d_%d",cmin[cbin],cmax[cbin],k), "", netabins, etabins);
            wnA[cbin][k] = new TH1D(Form("wnA_%d_%d_%d",cmin[cbin],cmax[cbin],k), "", netabins, etabins);
            wnB[cbin][k] = new TH1D(Form("wnB_%d_%d_%d",cmin[cbin],cmax[cbin],k), "", netabins, etabins);
            for (int ord = 1; ord<=3; ord++) {
                qABp[ord-1][cbin][k] = new TH1D(Form("qABp%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qABp[ord-1][cbin][k]->SetDirectory(0);
                qACp[ord-1][cbin][k] = new TH1D(Form("qACp%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qACp[ord-1][cbin][k]->SetDirectory(0);
                qBCp[ord-1][cbin][k] = new TH1D(Form("qBCp%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qBCp[ord-1][cbin][k]->SetDirectory(0);
                qABm[ord-1][cbin][k] = new TH1D(Form("qABm%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qABm[ord-1][cbin][k]->SetDirectory(0);
                qACm[ord-1][cbin][k] = new TH1D(Form("qACm%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qACm[ord-1][cbin][k]->SetDirectory(0);
                qBCm[ord-1][cbin][k] = new TH1D(Form("qBCm%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qBCm[ord-1][cbin][k]->SetDirectory(0);
                qABpcnt[ord-1][cbin][k] = new TH1D(Form("qABpcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qABpcnt[ord-1][cbin][k]->SetDirectory(0);
                qACpcnt[ord-1][cbin][k] = new TH1D(Form("qACpcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qACpcnt[ord-1][cbin][k]->SetDirectory(0);
                qBCpcnt[ord-1][cbin][k] = new TH1D(Form("qBCpcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qBCpcnt[ord-1][cbin][k]->SetDirectory(0);
                qABmcnt[ord-1][cbin][k] = new TH1D(Form("qABmcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qABmcnt[ord-1][cbin][k]->SetDirectory(0);
                qACmcnt[ord-1][cbin][k] = new TH1D(Form("qACmcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qACmcnt[ord-1][cbin][k]->SetDirectory(0);
                qBCmcnt[ord-1][cbin][k] = new TH1D(Form("qBCmcnt%d_%d_%d_%d",ord,cmin[cbin],cmax[cbin],k), "", 1, 0, 1);
                qBCmcnt[ord-1][cbin][k]->SetDirectory(0);
            }
        }
    }

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
        phiPsi1[nep] = new TH1D(Form("phiPsi%s1",EPName[nep].data()), "", 100, -3.6, 3.6);
        phiPsi2[nep] = new TH1D(Form("phiPsi%s2",EPName[nep].data()), "", 100, -3.6, 3.6);
        phiPsi3[nep] = new TH1D(Form("phiPsi%s3",EPName[nep].data()), "", 100, -3.6, 3.6);
        Psi1Psi[nep] = new TH1D(Form("Psi%s1Psi",EPName[nep].data()), "", 100, -3.6, 3.6);
        Psi2Psi[nep] = new TH1D(Form("Psi%s2Psi",EPName[nep].data()), "", 100, -3.6, 3.6);
        Psi3Psi[nep] = new TH1D(Form("Psi%s3Psi",EPName[nep].data()), "", 100, -3.6, 3.6);
    }

    ReadTree( etaweights, ptweights );


    //-- make plots

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


    TCanvas * cPsi = new TCanvas("cPsi","cPsi",800,400);
    cPsi->Divide(2,1);
    int psicol1[] = {kBlue, kMagenta, kGreen+2, kRed};
    for (int nep = 0; nep<4; nep++) {
        Psi1Psi[nep]->SetMarkerColor(psicol1[nep]);
        Psi2Psi[nep]->SetMarkerColor(psicol1[nep]);
        phiPsi1[nep]->SetMarkerColor(psicol1[nep]);
        phiPsi2[nep]->SetMarkerColor(psicol1[nep]);
        Psi1Psi[nep]->SetLineColor(psicol1[nep]);
        Psi2Psi[nep]->SetLineColor(psicol1[nep]);
        phiPsi1[nep]->SetLineColor(psicol1[nep]);
        phiPsi2[nep]->SetLineColor(psicol1[nep]);
    }
    cPsi->cd(1);
    Psi2Psi[1]->SetXTitle("#Psi_{n} - #Psi_{RP}");
    Psi2Psi[1]->Draw();
    for (int nep = 0; nep<4; nep++) {
        Psi2Psi[nep]->Draw("same");
        Psi1Psi[nep]->Draw("same");
    }
    cPsi->cd(2);
    phiPsi2[1]->SetXTitle("#phi - #Psi_{n}");
    phiPsi2[1]->Draw();
    for (int nep = 0; nep<4; nep++) {
        phiPsi2[nep]->Draw("same");
        phiPsi1[nep]->Draw("same");
    }


    TCanvas * cCenttest = new TCanvas("cCenttest","cCenttest",600,550);
    cCenttest->cd(1);
    centbins->SetXTitle("Centrality (%)");
    centbins->Draw();


}
