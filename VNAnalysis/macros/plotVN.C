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

        v1_pT_eta_0_8_neg[cbin]->Scale(1/2.);
        v1_pT_eta_0_8_pos[cbin]->Scale(1/2.);
        v1_pT_eta_0_24_neg[cbin]->Scale(1/6.);
        v1_pT_eta_0_24_pos[cbin]->Scale(1/6.);
        v2_pT_eta_0_8_av[cbin]->Scale(1/4.);
        v2_pT_eta_0_24_av[cbin]->Scale(1/12.);

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

    finDataEta = new TFile("../../../2015_PbPb/MH_v2/macros/hists/MH_combined_Eta.root","read");
    finDataPt = new TFile("../../..//2015_PbPb/MH_v2/macros/hists/MH_combined_Pt.root","read");
    for (int cbin = 0; cbin<NCbins; cbin++) {
        TString ctag = Form("%d_%d",(int)centbins[cbin],(int)centbins[cbin+1]);
        data_v1_eta[cbin] = (TH1D *) finDataEta->Get(Form("MH_nominal/%s/N1SUB2_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_pos[cbin] = (TH1D *) finDataPt->Get(Form("MH_nominal/eta_0_24/%s/N1SUB2_eta_0_24_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_neg[cbin] = (TH1D *) finDataPt->Get(Form("MH_nominal/eta_-24_0/%s/N1SUB2_eta_-24_0_%s",ctag.Data(),ctag.Data()));
        data_v1_pT_eta_0_24_av[cbin] = (TH1D *) data_v1_pT_eta_0_24_pos[cbin]->Clone(Form("N1SUB2_eta_-24_24_%s",ctag.Data()));
        data_v1_pT_eta_0_24_av[cbin]->Add(data_v1_pT_eta_0_24_neg[cbin],-1);
        data_v1_pT_eta_0_24_av[cbin]->Scale(0.5);

        data_v1_pT_112_0_24[cbin] = (TH1D *) finDataPt->Get(Form("MH_nominal/eta_0_24/%s/N112ASUB2_eta_0_24_%s",ctag.Data(),ctag.Data()));
    }

    if (!fopen("figures/ampt","r")) system("mkdir figures/ampt");

    # include "../../../2015_PbPb/published_results/PhysRevLett101_252301.h"

    int setcent = 4;

    TCanvas * c0 = new TCanvas("c0","c0",600,550);
    TPad * pad0 = (TPad *) c0->cd();
    pad0->SetGrid();
    TH1D * h0 = new TH1D("h0", "", 100, -2.5, 2.5);
    h0->SetStats(0);
    h0->SetXTitle("#eta");
    h0->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h0->GetYaxis()->SetRangeUser(-0.015, 0.015);
    h0->Draw();
    v1true_eta[setcent]->SetMarkerColor(kOrange+7);
    v1true_eta[setcent]->SetLineColor(kOrange+7);
    //v1true_eta[setcent]->SetFillColor(kOrange+7);
    //v1true_eta[setcent]->SetFillStyle(1001);
    //v1true_eta[setcent]->Draw("same E3");
    v1true_eta[setcent]->SetMarkerStyle(21);
    v1true_eta[setcent]->SetMarkerSize(1.2);
    v1true_eta[setcent]->Draw("same hist c");
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
    leg0->AddEntry(v1true_eta[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg0->Draw();
    c0->Print(Form("figures/ampt/compare_PbPb_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    TCanvas * c1 = new TCanvas("c1","c1",600,550);
    TPad * pad1 = (TPad *) c1->cd();
    pad1->SetGrid();
    TH1D * h1 = new TH1D("h1", "", 100, 0, 12);
    h1->SetStats(0);
    h1->SetXTitle("p_{T} (GeV/c)");
    h1->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h1->GetYaxis()->SetRangeUser(-0.04, 0.02);
    h1->Draw();
    v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kOrange+7);
    v1_pT_eta_0_24_av[setcent]->SetLineColor(kOrange+7);
    // v1_pT_eta_0_24_av[setcent]->SetFillColor(kOrange+7);
    // v1_pT_eta_0_24_av[setcent]->SetFillStyle(1001);
    //v1_pT_eta_0_24_av[setcent]->Draw("same E3");
    v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    v1_pT_eta_0_24_av[setcent]->Draw("same");
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetLineColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    data_v1_pT_eta_0_24_av[setcent]->Draw("same");
    TPaveText * tx1 = new TPaveText(0.20, 0.81, 0.37, 0.92, "NDC");
    SetTPaveTxt(tx1, 20);
    tx1->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    tx1->AddText("|#eta| < 2.4");
    tx1->Draw();
    TLegend * leg1 = new TLegend(0.36, 0.80, 0.64, 0.93);
    SetLegend(leg1, 20);
    leg1->AddEntry(data_v1_pT_eta_0_24_av[setcent],"PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    leg1->AddEntry(v1_pT_eta_0_24_av[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg1->Draw();
    c1->Print(Form("figures/ampt/compare_PbPb_pT_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    setcent = 5;
    TCanvas * c2 = new TCanvas("c2","c2",600,550);
    TPad * pad2 = (TPad *) c2->cd();
    pad2->SetGrid();
    TH1D * h2 = new TH1D("h2", "", 100, -2.5, 2.5);
    h2->SetStats(0);
    h2->SetXTitle("#eta");
    h2->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h2->GetYaxis()->SetRangeUser(0.0, 0.10);
    h2->Draw();
    v2true_eta[setcent]->SetMarkerColor(kOrange+7);
    v2true_eta[setcent]->SetLineColor(kOrange+7);
    //v2true_eta[setcent]->SetFillColor(kOrange+7);
    //v2true_eta[setcent]->SetFillStyle(1001);
    //v2true_eta[setcent]->Draw("same E3");
    v2true_eta[setcent]->SetMarkerStyle(21);
    v2true_eta[setcent]->SetMarkerSize(1.2);
    v2true_eta[setcent]->Draw("same");
    # include "../../../2015_PbPb/published_results/HIN-10-002.h"
    TGraphErrors * v2HIN_10_002_eta_20_25 = new TGraphErrors(12, v2eta_points, v2Ecent20to25, 0, v2Ecent20to25Err);
    v2HIN_10_002_eta_20_25->SetMarkerColor(kBlue);
    v2HIN_10_002_eta_20_25->SetLineColor(kBlue);
    v2HIN_10_002_eta_20_25->SetMarkerStyle(21);
    v2HIN_10_002_eta_20_25->SetMarkerSize(1.2);
    v2HIN_10_002_eta_20_25->Draw("same p");
    TPaveText * tx2 = new TPaveText(0.20, 0.19, 0.50, 0.30, "NDC");
    SetTPaveTxt(tx2, 20);
    tx2->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    tx2->AddText("0.3 < p_{T} < 3.0 GeV/c");
    tx2->Draw();
    TLegend * leg2 = new TLegend(0.50, 0.19, 0.78, 0.30);
    SetLegend(leg2, 20);
    leg2->AddEntry(v2HIN_10_002_eta_20_25,"HIN-10-002","p");
    leg2->AddEntry(v2true_eta[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    leg2->Draw();
    c2->Print(Form("figures/ampt/compare_v2_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    setcent = 0;
    TCanvas * c3 = new TCanvas("c3","c3",600,550);
    TPad * pad3 = (TPad *) c3->cd();
    pad3->SetGrid();
    TH1D * h3 = new TH1D("h3", "", 100, 0, 4);
    h3->SetStats(0);
    h3->SetXTitle("p_{T} (GeV/c)");
    h3->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h3->GetYaxis()->SetRangeUser(-0.006, 0.006);
    h3->Draw();
    v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kOrange+7);
    v1_pT_eta_0_24_av[setcent]->SetLineColor(kOrange+7);
    v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    v1_pT_eta_0_24_av[setcent]->Draw("same");
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetLineColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    data_v1_pT_eta_0_24_av[setcent]->Draw("same");
    TH1D * hSTAR_pT_0_5 = new TH1D("hSTAR_pT_0_5", "", 8, STAR_AuAu_200_TPC_cent0_5_pbin);
    for (int i = 0; i<8; i++) {
        hSTAR_pT_0_5->SetBinContent(i+1, STAR_AuAu_200_TPC_cent0_5_pT[i]);
        hSTAR_pT_0_5->SetBinError(i+1, STAR_AuAu_200_TPC_cent0_5_pTerr[i]);
    }
    hSTAR_pT_0_5->SetMarkerColor(kRed);
    hSTAR_pT_0_5->SetLineColor(kRed);
    hSTAR_pT_0_5->SetMarkerStyle(30);
    hSTAR_pT_0_5->SetMarkerSize(1.6);
    hSTAR_pT_0_5->Draw("same");
    TLegend * leg3 = new TLegend(0.19, 0.77, 0.47, 0.93);
    SetLegend(leg3, 20);
    leg3->AddEntry(data_v1_pT_eta_0_24_av[setcent],Form("PbPb #sqrt{s_{NN}} = 5.02 TeV |#eta| < 2.4 (%d-%d%%)",(int)centbins[setcent],(int)centbins[setcent+1]),"p");
    leg3->AddEntry(hSTAR_pT_0_5,"AuAu #sqrt{s_{NN}} = 200 GeV |#eta| < 1.3 (0-5%)","p");
    leg3->AddEntry(v1_pT_eta_0_24_av[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg3->Draw();
    c3->Print(Form("figures/ampt/compare_PbPb_STAR_pT_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    setcent = 6;
    TCanvas * c4 = new TCanvas("c4","c4",600,550);
    TPad * pad4 = (TPad *) c4->cd();
    pad4->SetGrid();
    TH1D * h4 = new TH1D("h4", "", 100, 0, 4);
    h4->SetStats(0);
    h4->SetXTitle("p_{T} (GeV/c)");
    h4->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h4->GetYaxis()->SetRangeUser(-0.015, 0.01);
    h4->Draw();
    v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kOrange+7);
    v1_pT_eta_0_24_av[setcent]->SetLineColor(kOrange+7);
    v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    v1_pT_eta_0_24_av[setcent]->Draw("same");
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetLineColor(kBlue);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    data_v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    data_v1_pT_eta_0_24_av[setcent]->Draw("same");
    TH1D * hSTAR_pT_5_40 = new TH1D("hSTAR_pT_5_40", "", 8, STAR_AuAu_200_TPC_cent5_40_pbin);
    for (int i = 0; i<8; i++) {
        hSTAR_pT_5_40->SetBinContent(i+1, STAR_AuAu_200_TPC_cent5_40_pT[i]);
        hSTAR_pT_5_40->SetBinError(i+1, STAR_AuAu_200_TPC_cent5_40_pTerr[i]);
    }
    hSTAR_pT_5_40->SetMarkerColor(kRed);
    hSTAR_pT_5_40->SetLineColor(kRed);
    hSTAR_pT_5_40->SetMarkerStyle(30);
    hSTAR_pT_5_40->SetMarkerSize(1.6);
    hSTAR_pT_5_40->Draw("same");
    TLegend * leg4 = new TLegend(0.19, 0.77, 0.47, 0.93);
    SetLegend(leg4, 20);
    leg4->AddEntry(data_v1_pT_eta_0_24_av[setcent],Form("PbPb #sqrt{s_{NN}} = 5.02 TeV |#eta| < 2.4 (%d-%d%%)",(int)centbins[setcent],(int)centbins[setcent+1]),"p");
    leg4->AddEntry(hSTAR_pT_5_40,"AuAu #sqrt{s_{NN}} = 200 GeV |#eta| < 1.3 (5-40%)","p");
    leg4->AddEntry(v1_pT_eta_0_24_av[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg4->Draw();
    c4->Print(Form("figures/ampt/compare_PbPb_STAR_pT_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    setcent = 0;
    TCanvas * c5 = new TCanvas("c5","c5",600,550);
    TPad * pad5 = (TPad *) c5->cd();
    pad5->SetGrid();
    TH1D * h5 = new TH1D("h5", "", 100, -2.5, 2.5);
    h5->SetStats(0);
    h5->SetXTitle("#eta");
    h5->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h5->GetYaxis()->SetRangeUser(-0.007, 0.007);
    h5->Draw();
    v1true_eta[setcent]->SetMarkerColor(kOrange+7);
    v1true_eta[setcent]->SetLineColor(kOrange+7);
    //v1true_eta[setcent]->SetFillColor(kOrange+7);
    //v1true_eta[setcent]->SetFillStyle(1001);
    //v1true_eta[setcent]->Draw("same E3");
    v1true_eta[setcent]->SetMarkerStyle(21);
    v1true_eta[setcent]->SetMarkerSize(1.2);
    v1true_eta[setcent]->Draw("same hist c");
    v1true_eta[setcent]->Draw("same");
    data_v1_eta[setcent]->SetMarkerColor(kBlue);
    data_v1_eta[setcent]->SetLineColor(kBlue);
    data_v1_eta[setcent]->SetMarkerStyle(21);
    data_v1_eta[setcent]->SetMarkerSize(1.2);
    data_v1_eta[setcent]->Draw("same");
    TH1D * hSTAR_eta_0_5 = new TH1D("hSTAR_eta_0_5", "", 6, STAR_AuAu_200_cent0_5_eta);
    for (int i = 0; i<6; i++) {
        hSTAR_eta_0_5->SetBinContent(i+1, STAR_AuAu_200_cent0_5_v1eta[i]);
        hSTAR_eta_0_5->SetBinError(i+1, STAR_AuAu_200_cent0_5_v1etaErr[i]);
    }
    hSTAR_eta_0_5->SetMarkerColor(kRed);
    hSTAR_eta_0_5->SetLineColor(kRed);
    hSTAR_eta_0_5->SetMarkerStyle(30);
    hSTAR_eta_0_5->SetMarkerSize(1.6);
    hSTAR_eta_0_5->Draw("same");
    TPaveText * tx5 = new TPaveText(0.62, 0.79, 0.92, 0.90, "NDC");
    SetTPaveTxt(tx5, 20);
    tx5->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    tx5->AddText("0.3 < p_{T} < 3.0 GeV/c");
    tx5->Draw();
    TLegend * leg5 = new TLegend(0.19, 0.18, 0.47, 0.34);
    SetLegend(leg5, 20);
    leg5->AddEntry(data_v1_eta[setcent],"PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    leg5->AddEntry(hSTAR_eta_0_5,"AuAu #sqrt{s_{NN}} = 200 GeV (0-5%)","p");
    leg5->AddEntry(v1true_eta[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg5->Draw();
    c5->Print(Form("figures/ampt/compare_PbPb_STAR_eta_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    setcent = 6;
    TCanvas * c6 = new TCanvas("c6","c6",600,550);
    TPad * pad6 = (TPad *) c6->cd();
    pad6->SetGrid();
    TH1D * h6 = new TH1D("h6", "", 100, -2.5, 2.5);
    h6->SetStats(0);
    h6->SetXTitle("#eta");
    h6->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    h6->GetYaxis()->SetRangeUser(-0.015, 0.015);
    h6->Draw();
    v1true_eta[setcent]->SetMarkerColor(kOrange+7);
    v1true_eta[setcent]->SetLineColor(kOrange+7);
    //v1true_eta[setcent]->SetFillColor(kOrange+7);
    //v1true_eta[setcent]->SetFillStyle(1001);
    //v1true_eta[setcent]->Draw("same E3");
    v1true_eta[setcent]->SetMarkerStyle(21);
    v1true_eta[setcent]->SetMarkerSize(1.2);
    v1true_eta[setcent]->Draw("same hist c");
    v1true_eta[setcent]->Draw("same");
    data_v1_eta[setcent]->SetMarkerColor(kBlue);
    data_v1_eta[setcent]->SetLineColor(kBlue);
    data_v1_eta[setcent]->SetMarkerStyle(21);
    data_v1_eta[setcent]->SetMarkerSize(1.2);
    data_v1_eta[setcent]->Draw("same");
    TH1D * hSTAR_eta_5_40 = new TH1D("hSTAR_eta_0_5", "", 8, STAR_AuAu_200_cent5_40_eta);
    for (int i = 0; i<8; i++) {
        hSTAR_eta_5_40->SetBinContent(i+1, STAR_AuAu_200_cent5_40_v1eta[i]);
        hSTAR_eta_5_40->SetBinError(i+1, STAR_AuAu_200_cent5_40_v1etaErr[i]);
    }
    hSTAR_eta_5_40->SetMarkerColor(kRed);
    hSTAR_eta_5_40->SetLineColor(kRed);
    hSTAR_eta_5_40->SetMarkerStyle(30);
    hSTAR_eta_5_40->SetMarkerSize(1.6);
    hSTAR_eta_5_40->Draw("same");
    TPaveText * tx6 = new TPaveText(0.62, 0.79, 0.92, 0.90, "NDC");
    SetTPaveTxt(tx6, 20);
    tx6->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    tx6->AddText("0.3 < p_{T} < 3.0 GeV/c");
    tx6->Draw();
    TLegend * leg6 = new TLegend(0.19, 0.18, 0.47, 0.34);
    SetLegend(leg6, 20);
    leg6->AddEntry(data_v1_eta[setcent],"PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    leg6->AddEntry(hSTAR_eta_0_5,"AuAu #sqrt{s_{NN}} = 200 GeV (5-40%)","p");
    leg6->AddEntry(v1true_eta[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    leg6->Draw();
    c6->Print(Form("figures/ampt/compare_PbPb_STAR_eta_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");


    // TCanvas * c7 = new TCanvas("c7","c7",600,550);
    // TPad * pad7 = (TPad *) c7->cd();
    // pad7->SetGrid();
    // TH1D * h7 = new TH1D("h7", "", 100, 0, 12);
    // h7->SetStats(0);
    // h7->SetXTitle("p_{T} (GeV/c)");
    // h7->SetYTitle("<<cos(#phi - #Psi_{RP})>>");
    // h7->GetYaxis()->SetRangeUser(-0.04, 0.02);
    // h7->Draw();
    // v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kOrange+7);
    // v1_pT_eta_0_24_av[setcent]->SetLineColor(kOrange+7);
    // // v1_pT_eta_0_24_av[setcent]->SetFillColor(kOrange+7);
    // // v1_pT_eta_0_24_av[setcent]->SetFillStyle(1001);
    // //v1_pT_eta_0_24_av[setcent]->Draw("same E3");
    // v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    // v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    // v1_pT_eta_0_24_av[setcent]->Draw("same");
    // data_v1_pT_eta_0_24_av[setcent]->SetMarkerColor(kBlue);
    // data_v1_pT_eta_0_24_av[setcent]->SetLineColor(kBlue);
    // data_v1_pT_eta_0_24_av[setcent]->SetMarkerStyle(21);
    // data_v1_pT_eta_0_24_av[setcent]->SetMarkerSize(1.2);
    // data_v1_pT_eta_0_24_av[setcent]->Draw("same");
    // hSTAR_pT_5_40->SetMarkerColor(kRed);
    // hSTAR_pT_5_40->SetLineColor(kRed);
    // hSTAR_pT_5_40->SetMarkerStyle(30);
    // hSTAR_pT_5_40->SetMarkerSize(1.6);
    // hSTAR_pT_5_40->Draw("same");
    // data_v1_pT_112_0_24[setcent]->SetMarkerColor(kGreen+3);
    // data_v1_pT_112_0_24[setcent]->SetLineColor(kGreen+3);
    // data_v1_pT_112_0_24[setcent]->SetMarkerStyle(28);
    // data_v1_pT_112_0_24[setcent]->SetMarkerSize(1.5);
    // data_v1_pT_112_0_24[setcent]->Draw("same");
    // TPaveText * tx7 = new TPaveText(0.20, 0.81, 0.37, 0.92, "NDC");
    // SetTPaveTxt(tx7, 20);
    // tx7->AddText(Form("%d-%d%%",(int)centbins[setcent],(int)centbins[setcent+1]));
    // tx7->AddText("|#eta| < 2.4");
    // tx7->Draw();
    // TLegend * leg7 = new TLegend(0.36, 0.80, 0.64, 0.93);
    // SetLegend(leg7, 20);
    // leg7->AddEntry(data_v1_pT_eta_0_24_av[setcent],"N1SUB2 PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    // leg7->AddEntry(data_v1_pT_112_0_24[setcent],"N112ASUB2 PbPb #sqrt{s_{NN}} = 5.02 TeV","p");
    // leg7->AddEntry(hSTAR_pT_0_5,"AuAu #sqrt{s_{NN}} = 200 GeV (5-40%)","p");
    // leg7->AddEntry(v1_pT_eta_0_24_av[setcent],"AMPT PbPb #sqrt{s_{NN}} = 5.02 TeV","lp");
    // leg7->Draw();
    // c7->Print(Form("figures/ampt/compare_PbPb_mix_pT_%d_%d.png",(int)centbins[setcent],(int)centbins[setcent+1]),"png");

}
