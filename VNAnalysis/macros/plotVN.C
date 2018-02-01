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

TH1D * v1_pT_eta_0_8_neg[NCbins];
TH1D * v1_pT_eta_0_8_pos[NCbins];
TH1D * v1_pT_eta_0_24_neg[NCbins];
TH1D * v1_pT_eta_0_24_pos[NCbins];
TH1D * v1_pT_eta_0_8_av[NCbins];
TH1D * v1_pT_eta_0_24_av[NCbins];
TH1D * v2_pT_eta_0_8_av[NCbins];
TH1D * v2_pT_eta_0_24_av[NCbins];

TH1D * data_v1_eta[NCbins];
TH1D * data_v1_pT_eta_0_24_pos[NCbins];
TH1D * data_v1_pT_eta_0_24_neg[NCbins];
TH1D * data_v1_pT_eta_0_24_av[NCbins];

TFile * fin;
TFile * finDataEta;
TFile * finDataPt;
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

        v1_pT_eta_0_8_neg[cbin] = v1true2D[cbin]->ProjectionX(Form("v1_pT_eta_0_8_neg_%s",ctag.Data()), 5, 6);
        v1_pT_eta_0_8_pos[cbin] = v1true2D[cbin]->ProjectionX(Form("v1_pT_eta_0_8_pos_%s",ctag.Data()), 7, 8);
        v1_pT_eta_0_24_neg[cbin] = v1true2D[cbin]->ProjectionX(Form("v1_pT_eta_0_24_neg_%s",ctag.Data()), 1, 6);
        v1_pT_eta_0_24_pos[cbin] = v1true2D[cbin]->ProjectionX(Form("v1_pT_eta_0_24_pos_%s",ctag.Data()), 7, 12);
        v2_pT_eta_0_8_av[cbin] = v2true2D[cbin]->ProjectionX(Form("v2_pT_eta_0_8_av_%s",ctag.Data()), 5, 8);
        v2_pT_eta_0_24_av[cbin] = v2true2D[cbin]->ProjectionX(Form("v2_pT_eta_0_24_av_%s",ctag.Data()), 1, 12);

        v1_pT_eta_0_8_av[cbin] = (TH1D *) v1_pT_eta_0_8_pos[cbin]->Clone(Form("v1_pT_eta_0_8_av_%s",ctag.Data()));
        v1_pT_eta_0_8_av[cbin]->Add(v1_pT_eta_0_8_neg[cbin],-1);
        v1_pT_eta_0_8_av[cbin]->Scale(0.5);

        v1_pT_eta_0_24_av[cbin] = (TH1D *) v1_pT_eta_0_24_pos[cbin]->Clone(Form("v1_pT_eta_0_24_av_%s",ctag.Data()));
        v1_pT_eta_0_24_av[cbin]->Add(v1_pT_eta_0_24_neg[cbin],-1);
        v1_pT_eta_0_24_av[cbin]->Scale(0.5);

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

    if (!fopen("figures","r")) system("mkdir figures");
    fout = new TFile("figures/outputVN.root","recreate");
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TDirectory * tdir = (TDirectory *) fout->mkdir(Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]));
        tdir->cd();
        v1true_eta[cbin]->Write();
        v2true_eta[cbin]->Write();
        v1_pT_eta_0_8_av[cbin]->Write();
        v1_pT_eta_0_24_av[cbin]->Write();
        v1_pT_eta_0_8_neg[cbin]->Write();
        v1_pT_eta_0_8_pos[cbin]->Write();
        v1_pT_eta_0_24_neg[cbin]->Write();
        v1_pT_eta_0_24_pos[cbin]->Write();
        v2_pT_eta_0_8_av[cbin]->Write();
        v2_pT_eta_0_24_av[cbin]->Write();
        for (int ebin = 0; ebin<netabins; ebin++) {
            TDirectory * tdire = (TDirectory *) tdir->mkdir(Form("eta_%1.1f_%1.1f",etabins[ebin],etabins[ebin+1]));
            tdire->cd();
            v1_pT[cbin][ebin]->Write();
            v2_pT[cbin][ebin]->Write();
        }
    }

    finDataEta = new TFile("/mnt/c/Users/willj/macros/v1flow/2015_PbPb/MH_v2/macros/hists/MH_combined_Eta.root","read");
    finDataPt = new TFile("/mnt/c/Users/willj/macros/v1flow/2015_PbPb/MH_v2/macros/hists/MH_combined_Pt.root","read");
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TString ctag = Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]);
        data_v1_eta[cbin] = (TH1D *) finDataEta->Get(Form("MH_nominal/%s/N1SUB2_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_pos[cbin] = (TH1D *) finDataPt->Get(Form("MH_nominal/eta_0_24/%s/N1SUB2_eta_0_24_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_neg[cbin] = (TH1D *) finDataPt->Get(Form("MH_nominal/eta_-24_0/%s/N1SUB2_eta_-24_0_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_av[cbin] = (TH1D *) data_v1_pT_eta_0_24_pos[cbin]->Clone(Form("N1SUB2_eta_-24_24_%s",ctag.Data()));
        data_v1_pT_eta_0_24_av[cbin]->Add(data_v1_pT_eta_0_24_neg[cbin]);
        data_v1_pT_eta_0_24_av[cbin]->Scale(0.5);
    }

    if (!fopen("figures/ampt","r")) system("mkdir figures/ampt");

    TCanvas * c0 = new TCanvas("c0","c0",600,550);
    TPad * pad0 = (TPad *) c0->cd();
    pad0->SetGrid();
    int setcent = 1;
    TH1D * h0 = new TH1D("h0", "", 100, -2.5, 2.5);
    h0->SetStats(0);
    h0->SetXTitle("#eta");
    h0->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h0->GetYaxis()->SetRangeUser(-0.015, 0.015);
    h0->Draw();
    v1true_eta[setcent]->SetMarkerColor(kOrange+1);
    v1true_eta[setcent]->SetLineColor(kOrange+1);
    v1true_eta[setcent]->SetLineWidth(5);
    v1true_eta[setcent]->SetFillColor(kOrange+1);
    v1true_eta[setcent]->SetFillStyle(1001);
    v1true_eta[setcent]->Draw("same E3");
    v1true_eta[setcent]->Draw("same");
    data_v1_eta[setcent]->SetMarkerColor(kBlue);
    data_v1_eta[setcent]->SetLineColor(kBlue);
    data_v1_eta[setcent]->SetMarkerStyle(21);
    data_v1_eta[setcent]->SetMarkerSize(1.2);
    data_v1_eta[setcent]->Draw("same");
    TPaveText * tx0 = new TPaveText(0.62, 0.79, 0.92, 0.90, "NDC");
    SetTPaveTxt(tx0, 20);
    tx0->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    tx0->AddText("0.3 < p_{T} < 3.0 GeV/c");
    tx0->Draw();
    TLegend * leg0 = new TLegend(0.20, 0.18, 0.48, 0.31);
    SetLegend(leg0, 20);
    leg0->AddEntry(data_v1_eta[setcent],"PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    leg0->AddEntry(v1true_eta[setcent],"AMPT with string melting","l");
    leg0->Draw();
    c0->Print(Form("figures/ampt/compare_PbPb_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");

}
