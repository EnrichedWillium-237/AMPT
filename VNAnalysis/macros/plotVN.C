# include "TCanvas.h"
# include "TFile.h"
# include "TGraphErrors.h"
# include "TH1.h"
# include "TH2.h"
# include "TLeaf.h"
# include "TMath.h"
# include "TString.h"
# include "TStyle.h"
# include <cmath>
# include <fstream>
# include <iostream>
# include <vector>

using namespace std;

static const int ncentbins = 14;
static const int cminCENT[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60,  0, 20,  60};
static const int cmaxCENT[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 20, 60, 100};
static const int NCbins = 11;
static const double centbins[] = {0, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70};
static const int nptbins = 18;
static const double ptbins[] = {0.30,  0.40,  0.50,  0.60,  0.80,  1.00,  1.25,  1.50,  2.00,  2.50,  3.00,
    3.50,  4.00,  5.00,  6.00,  7.00,  8.00,  10.00,  12.00};
static const int netabins = 12;
static const double etabins[] = {-2.4, -2.0, -1.6, -1.2, -0.8, -0.4,  0.0,  0.4,  0.8,  1.2,  1.6,  2.0,  2.4};

TH2D * v1true2D[NCbins];
TH2D * v2true2D[NCbins];
TH2D * v1raw2D[NCbins];
TH2D * v2raw2D[NCbins];
TH2D * qcnt[NCbins];

TH1D * v1_pT[NCbins][netabins];
TH1D * v2_pT[NCbins][netabins];
TH1D * v1true_eta[NCbins];
TH1D * v2true_eta[NCbins];

TH1D * q1;
TH1D * q2;
TH1D * w0;

TFile * fin;
TFile * fout;

# include "style.h"

void plotVN() {

    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    fin = new TFile("hists/amptVN.root","read");

    for (int cbin = 0; cbin<NCbins; cbin++) {
        TString ctag = Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]);
        v1true2D[cbin] = (TH2D *) fin->Get(Form("%s/v1true_%s",ctag.Data(),ctag.Data()));
        v2true2D[cbin] = (TH2D *) fin->Get(Form("%s/v2true_%s",ctag.Data(),ctag.Data()));
        v1raw2D[cbin] = (TH2D *) fin->Get(Form("%s/v1raw_%s",ctag.Data(),ctag.Data()));
        v2raw2D[cbin] = (TH2D *) fin->Get(Form("%s/v2raw_%s",ctag.Data(),ctag.Data()));
        qcnt[cbin] = (TH2D *) fin->Get(Form("%s/qcnt_%s",ctag.Data(),ctag.Data()));

        v1true_eta[cbin] = new TH1D(Form("v1true_eta_%s",ctag.Data()), "", netabins, etabins);
        v2true_eta[cbin] = new TH1D(Form("v2true_eta_%s",ctag.Data()), "", netabins, etabins);

        for (int ebin = 0; ebin<netabins; ebin++) {
            v1_pT[cbin][ebin] = v1true2D[cbin]->ProjectionX(Form("v1_pT_eta_%1.1f_%1.1f_%s",etabins[ebin],etabins[ebin+1],ctag.Data()), ebin+1, ebin+1);
            v2_pT[cbin][ebin] = v2true2D[cbin]->ProjectionX(Form("v2_pT_eta_%1.1f_%1.1f_%s",etabins[ebin],etabins[ebin+1],ctag.Data()), ebin+1, ebin+1);

            // compute integral v1(eta)
            double v1int = 0;
            double v1inte = 0;
            double v2int = 0;
            double v2inte = 0;
            TH1D * yld = (TH1D *) qcnt[cbin]->ProjectionX("yld", ebin+1, ebin+1);
            double y1[20];
            double y2[20];
            double ey1[20];
            double ey2[20];
            for (int i = 0; i<20; i++) {
                y1[20] = 0;
                y2[20] = 0;
                ey1[20] = 0;
                ey2[20] = 0;
            }
            int npt = 0;
            double wv1 = 0;
            double wv1e = 0;
            double wv2 = 0;
            double wv2e = 0;
            double w = 0;
            for (int i = 1; i<=10; i++) {
                y1[npt] = v1_pT[cbin][ebin]->GetBinContent(i);
                y2[npt] = v2_pT[cbin][ebin]->GetBinContent(i);
                ey1[npt] = v1_pT[cbin][ebin]->GetBinError(i);
                ey2[npt] = v2_pT[cbin][ebin]->GetBinError(i);
                wv1  += y1[npt]*yld->GetBinContent(i);
                wv1e += ey1[npt]*yld->GetBinContent(i);
                wv2  += y2[npt]*yld->GetBinContent(i);
                wv2e += ey2[npt]*yld->GetBinContent(i);
                w    += yld->GetBinContent(i);
                ++npt;
            }
            yld->Delete();
            v1int = wv1/w;
            v1inte = wv1e/w;
            v2int = wv2/w;
            v2inte = wv2e/w;

            v1true_eta[cbin]->SetBinContent(ebin+1, v1int);
            v1true_eta[cbin]->SetBinError(ebin+1, v1inte);
            v2true_eta[cbin]->SetBinContent(ebin+1, v2int);
            v2true_eta[cbin]->SetBinError(ebin+1, v2inte);
        }
    }

    // compute integral v1(eta)
    for (int cbin = 0; cbin<NCbins; cbin++) {

    }

    if (!fopen("figures","r")) system("mkdir figures");
    fout = new TFile("figures/outputVN.root","recreate");
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TDirectory * tdir = (TDirectory *) fout->mkdir(Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]));
        tdir->cd();
        v1true_eta[cbin]->Write();
        v2true_eta[cbin]->Write();
        for (int ebin = 0; ebin<netabins; ebin++) {
            TDirectory * tdire = (TDirectory *) tdir->mkdir(Form("eta_%1.1f_%1.1f",etabins[ebin],etabins[ebin+1]));
            tdire->cd();
            v1_pT[cbin][ebin]->Write();
            v2_pT[cbin][ebin]->Write();
        }
    }

}
