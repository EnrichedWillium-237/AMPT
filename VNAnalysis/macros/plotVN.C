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

static const int ncentbins = 4;
static const int cminCENT[] = {0,  5, 10, 70};
static const int cmaxCENT[] = {5, 10, 70, 100};
static const int NCbins = 4;
static const double centbins[] = {0, 5, 10, 70, 100};
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
TH1D * data_v1_pT_112_0_24[NCbins];

TFile * fin;
TFile * finDataEta;
TFile * finDataPt;
TFile * fout;

# include "style.h"

void plotVN() {

    TH1::SetDefaultSumw2();
    TH2::SetDefaultSumw2();

    fin = new TFile("hists/amptVN.root","read");

    TString ctag = Form("%d_%d",10,70);
    v1true2D[1] = (TH2D *) fin->Get("10_70/v1true_40_80");
    v2true2D[1] = (TH2D *) fin->Get("10_70/v2true_40_80");
    v1raw2D[1] = (TH2D *) fin->Get("10_70/v1raw_40_80");
    v2raw2D[1] = (TH2D *) fin->Get("10_70/v2raw_40_80");
    qcnt[1] = (TH2D *) fin->Get("10_70/qcnt_40_80");

    v1true_eta[1] = new TH1D(Form("v1true_eta_%s",ctag.Data()), "", netabins, etabins);
    v2true_eta[1] = new TH1D(Form("v2true_eta_%s",ctag.Data()), "", netabins, etabins);

    v1_pT_eta_0_8_neg[1] = v1true2D[1]->ProjectionX(Form("v1_pT_eta_0_8_neg_%s",ctag.Data()), 5, 6);
    v1_pT_eta_0_8_pos[1] = v1true2D[1]->ProjectionX(Form("v1_pT_eta_0_8_pos_%s",ctag.Data()), 7, 8);
    v1_pT_eta_0_24_neg[1] = v1true2D[1]->ProjectionX(Form("v1_pT_eta_0_24_neg_%s",ctag.Data()), 1, 6);
    v1_pT_eta_0_24_pos[1] = v1true2D[1]->ProjectionX(Form("v1_pT_eta_0_24_pos_%s",ctag.Data()), 7, 12);
    v2_pT_eta_0_8_av[1] = v2true2D[1]->ProjectionX(Form("v2_pT_eta_0_8_av_%s",ctag.Data()), 5, 8);
    v2_pT_eta_0_24_av[1] = v2true2D[1]->ProjectionX(Form("v2_pT_eta_0_24_av_%s",ctag.Data()), 1, 12);

    v1_pT_eta_0_8_neg[1]->Scale(1/2.);
    v1_pT_eta_0_8_pos[1]->Scale(1/2.);
    v1_pT_eta_0_24_neg[1]->Scale(1/6.);
    v1_pT_eta_0_24_pos[1]->Scale(1/6.);
    v2_pT_eta_0_8_av[1]->Scale(1/4.);
    v2_pT_eta_0_24_av[1]->Scale(1/12.);

    v1_pT_eta_0_8_av[1] = (TH1D *) v1_pT_eta_0_8_pos[1]->Clone(Form("v1_pT_eta_0_8_av_%s",ctag.Data()));
    v1_pT_eta_0_8_av[1]->Add(v1_pT_eta_0_8_neg[1],-1);
    v1_pT_eta_0_8_av[1]->Scale(0.5);

    v1_pT_eta_0_24_av[1] = (TH1D *) v1_pT_eta_0_24_pos[1]->Clone(Form("v1_pT_eta_0_24_av_%s",ctag.Data()));
    v1_pT_eta_0_24_av[1]->Add(v1_pT_eta_0_24_neg[1],-1);
    v1_pT_eta_0_24_av[1]->Scale(0.5);

    for (int ebin = 0; ebin<netabins; ebin++) {
        v1_pT[1][ebin] = v1true2D[1]->ProjectionX(Form("v1_pT_eta_%1.1f_%1.1f_%s",etabins[ebin],etabins[ebin+1],ctag.Data()), ebin+1, ebin+1);
        v2_pT[1][ebin] = v2true2D[1]->ProjectionX(Form("v2_pT_eta_%1.1f_%1.1f_%s",etabins[ebin],etabins[ebin+1],ctag.Data()), ebin+1, ebin+1);

        // compute integral v1(eta)
        double v1int = 0;
        double v1inte = 0;
        double v2int = 0;
        double v2inte = 0;
        TH1D * yld = (TH1D *) qcnt[1]->ProjectionX("yld", ebin+1, ebin+1);
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
            y1[npt] = v1_pT[1][ebin]->GetBinContent(i);
            y2[npt] = v2_pT[1][ebin]->GetBinContent(i);
            ey1[npt] = v1_pT[1][ebin]->GetBinError(i);
            ey2[npt] = v2_pT[1][ebin]->GetBinError(i);
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

        // v1true_eta[1]->SetBinContent(ebin+1, v1int);
        // v1true_eta[1]->SetBinError(ebin+1, v1inte);
        // v2true_eta[1]->SetBinContent(ebin+1, v2int);
        // v2true_eta[1]->SetBinError(ebin+1, v2inte);

        v1true_eta[1]->SetBinContent(ebin+1, v1int);
        v1true_eta[1]->SetBinError(ebin+1, v1inte);
        v2true_eta[1]->SetBinContent(ebin+1, v2int);
        v2true_eta[1]->SetBinError(ebin+1, v2inte);
    }

    TFile * fout = new TFile("ampt_true.root","recreate");
    fout->cd();
    v1true_eta[1]->Write();
    v2true_eta[1]->Write();


    // TFile * fincms_eta = new TFile("/mnt/c/Users/willj/Physics/PhysicsKU/AN-16-293/myDir/notes/HIN-17-009/trunk/data/data_fig6.root","read");
    // TGraphErrors * v1oddCMS_eta = (TGraphErrors *) fincms_eta->Get("N1HFfSUB2/-2.0_2.0/10_70/gint");
    // v1oddCMS_eta->SetMarkerStyle(21);
    // v1oddCMS_eta->SetMarkerSize(1.2);
    // v1oddCMS_eta->SetMarkerColor(kBlue);
    // v1oddCMS_eta->SetLineColor(kBlue);


    // TFile * fincms_pt = new TFile("/mnt/c/Users/willj/Physics/PhysicsKU/AN-16-293/myDir/notes/HIN-17-009/trunk/data/data_fig1.root","read");
    // TGraphErrors * v1oddCMS_pt = (TGraphErrors *) fincms_pt->Get("N1HFfSUB2/0.0_2.0/10_15/g");
    // v1oddCMS_pt->SetMarkerStyle(21);
    // v1oddCMS_pt->SetMarkerSize(1.2);
    // v1oddCMS_pt->SetMarkerColor(kBlue);
    // v1oddCMS_pt->SetLineColor(kBlue);
    // cout<<"here2"<<endl;
    //
    // TFile * finALICE = new TFile("/mnt/c/Users/willj/Physics/PhysicsKU/AN-16-293/myDir/notes/HIN-17-009/trunk/data/PRL_111_232302.root","read");
    // TH1D * ALICE_v1odd_eta_c10_60 = (TH1D *) finALICE->Get("ALICE_v1odd_eta_c10_60");
    // ALICE_v1odd_eta_c10_60->SetMarkerStyle(25);
    // ALICE_v1odd_eta_c10_60->SetMarkerSize(1.2);
    // ALICE_v1odd_eta_c10_60->SetMarkerColor(kMagenta);
    // ALICE_v1odd_eta_c10_60->SetLineColor(kMagenta);
    // cout<<"here3"<<endl;



    // TCanvas * c0 = new TCanvas("c0", "c0", 650, 600);
    // c0->cd();
    // TH1D * h0 = new TH1D("h0", "h0", 100, -2.1, 2.1);
    // h0->SetXTitle("#eta");
    // h0->SetYTitle("v_{1}^{odd}");
    // h0->GetYaxis()->SetRangeUser(-0.012, 0.012);
    // h0->Draw();
    // v1true_eta[1]->SetMarkerStyle(20);
    // v1true_eta[1]->SetMarkerSize(1.3);
    // v1true_eta[1]->SetMarkerColor(kOrange+7);
    // v1true_eta[1]->SetLineColor(kOrange+7);
    // v1true_eta[1]->Draw("same p");
    // v1oddCMS_eta->Draw("same p");
    // ALICE_v1odd_eta_c10_60->Draw("same");
    // TLegend * leg0 = new TLegend(0.2, 0.2, 0.4, 0.4);
    // SetLegend(leg0, 20);
    // leg0->SetHeader("10 - 60%");
    // leg0->AddEntry(v1oddCMS_eta,"CMS, PbPb 5.02 TeV","p");
    // leg0->AddEntry(ALICE_v1odd_eta_c10_60,"ALICE, PbPb 2.76 TeV (Spectator)","p");
    // leg0->AddEntry(v1true_eta[1],"AMPT <cos(#phi - #Psi_{RP})>","p");
    // leg0->Draw();
    // c0->Print("figures/v1AMPT_eta.png","png");
    //
    //
    // TCanvas * c1 = new TCanvas("c1", "c1", 650, 600);
    // c1->cd();
    // TH1D * h1 = new TH1D("h1", "h1", 100, 0.0, 8.5);
    // h1->SetXTitle("p_{T} (GeV/c)");
    // h1->SetYTitle("v_{1}^{odd}");
    // h1->GetYaxis()->SetRangeUser(-0.04, 0.03);
    // h1->Draw();
    // v1_pT_eta_0_8_av[1]->SetMarkerStyle(20);
    // v1_pT_eta_0_8_av[1]->SetMarkerSize(1.3);
    // v1_pT_eta_0_8_av[1]->SetMarkerColor(kOrange+7);
    // v1_pT_eta_0_8_av[1]->SetLineColor(kOrange+7);
    // v1_pT_eta_0_8_av[1]->Draw("same p");
    // v1oddCMS_pt->Draw("same p");
    // TLegend * leg1 = new TLegend(0.2, 0.2, 0.4, 0.4);
    // SetLegend(leg1, 20);
    // leg1->SetHeader("|#eta| < 2 (10 - 60%)");
    // leg1->AddEntry(v1oddCMS_eta,"CMS, PbPb 5.02 TeV","p");
    // leg1->AddEntry(v1_pT_eta_0_8_av[1],"AMPT <cos(#phi - #Psi_{RP})>","p");
    // leg1->Draw();
    // c1->Print("figures/v1AMPT_pt.png","png");
    //
    //
    // TCanvas * c2 = new TCanvas("c2", "c2", 650, 600);
    // c2->cd();
    // TH1D * h2 = new TH1D("h2", "h2", 100, -2.1, 2.1);
    // h2->SetXTitle("p_{T} (GeV/c)");
    // h2->SetYTitle("v_{2}");
    // h2->GetYaxis()->SetRangeUser(0, 0.09);
    // h2->Draw();
    // v2true_eta[1]->SetMarkerStyle(20);
    // v2true_eta[1]->SetMarkerSize(1.3);
    // v2true_eta[1]->SetMarkerColor(kOrange+7);
    // v2true_eta[1]->SetLineColor(kOrange+7);
    // v2true_eta[1]->Draw("same");
    // c2->Print("figures/v2AMPT_eta.png","png");


}
