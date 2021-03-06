# include "TCanvas.h"
# include "TDirectory.h"
# include "TFile.h"
# include "TGraphErrors.h"
# include "TH1.h"
# include "TH2.h"
# include "TLatex.h"
# include "TLegend.h"
# include "TMath.h"
# include "TPaveText.h"
# include <iostream>

using namespace std;

static const int ncbins = 11;
static const int cmin[] = {0,  5, 10, 15, 20, 25, 30, 35, 40, 50, 60};
static const int cmax[] = {5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70};

void SetTPaveTxt( TPaveText * txtemplate, int txtsize ) {
  txtemplate->SetFillColor(0);
  txtemplate->SetBorderSize(0);
  txtemplate->SetTextFont(43);
  txtemplate->SetTextAlign(12);
  txtemplate->SetTextSize(txtsize);
}

void SetLegend( TLegend * legtemplate, int legsize ) {
  legtemplate->SetFillColor(0);
  legtemplate->SetBorderSize(0);
  legtemplate->SetTextFont(43);
  legtemplate->SetTextSize(legsize);
}

TFile * fin;
TFile * finSyst;
TH1D * h1;
TH1D * h2;
TGraphErrors * N1MCp22SUB3[ncbins];
TGraphErrors * N1MCm22SUB3[ncbins];
TGraphErrors * N1EVENSUB3[ncbins];
TGraphErrors * N1EVENSUB3_syst[ncbins];

void fig5A() {

    fin = new TFile("../data/data_fig5A.root");

    int col[] = {kRed, kOrange+5, kBlue, kGreen+2, kCyan+2, kMagenta, kBlack, kRed, kBlue, kGreen+2, kCyan+2};
    int mrkstyle[] =   {20,  25,  21,  28,  33,  27,  24,  34, 27,  20,  31};
    double mrksize[] = {1.3, 1.2, 1.2, 1.6, 1.8, 1.8, 1.2, 1.6, 1.8, 1.2, 1.4};

    for (int i = 0; i<ncbins; i++) {
        // N1MCp22SUB3[i] = (TGraphErrors *) fin->Get(Form("N1MCp22SUB3/-2.4_-0.4/%d_%d/gintA",cmin[i],cmax[i]));
        // N1MCm22SUB3[i] = (TGraphErrors *) fin->Get(Form("N1MCm22SUB3/0.4_2.4/%d_%d/gintA",cmin[i],cmax[i]));
        N1EVENSUB3[i] = (TGraphErrors *) fin->Get(Form("N1EVENSUB3/-2.4_2.4/%d_%d/gint",cmin[i],cmax[i]));
        // N1MCp22SUB3[i] = (TGraphErrors *) fin->Get(Form("N1MCp22SUB3/-2.0_0.0/%d_%d/gintA",cmin[i],cmax[i]));
        // N1MCm22SUB3[i] = (TGraphErrors *) fin->Get(Form("N1MCm22SUB3/0.0_2.0/%d_%d/gintA",cmin[i],cmax[i]));
        // Double_t xp[50], xm[50], yp[50], ym[50], yperr[50], ymerr[50], ypm[50], ypmerr[50];
        // int num = N1MCp22SUB3[i]->GetN();
        // for (int j = 0; j<num; j++) {
        //     N1MCp22SUB3[i]->GetPoint(j, xp[j], yp[j]);
        //     yperr[j] = N1MCp22SUB3[i]->GetErrorY(j);
        //
        //     N1MCm22SUB3[i]->GetPoint(j, xm[j], ym[j]);
        //     ymerr[j] = N1MCm22SUB3[i]->GetErrorY(j);
        //
        //     if (xp[j]<0.0) {
        //         ypm[j] = yp[j];
        //         ypmerr[j] = yperr[j];
        //     } else {
        //         ypm[j] = ym[j];
        //         ypmerr[j] = ymerr[j];
        //     }
        // }
        // N1EVENSUB3[i] = new TGraphErrors(num, xp, ypm, 0, ypmerr);
    }

    for (int i = 0; i<ncbins; i++) {
        N1EVENSUB3[i]->SetMarkerStyle(mrkstyle[i]);
        N1EVENSUB3[i]->SetMarkerSize(mrksize[i]);
        N1EVENSUB3[i]->SetMarkerColor(col[i]);
        N1EVENSUB3[i]->SetLineColor(col[i]);
    }


    //-- systematics
    finSyst = new TFile("../data/data_systematics.root","read");

    for (int i = 0; i<ncbins; i++) {
        Double_t x[50], y[50], xerr[50], ysyst[50];
        int num = N1EVENSUB3[i]->GetN();
        for (int j = 0; j<num; j++) {
            N1EVENSUB3[i]->GetPoint(j, x[j], y[j]);
            xerr[j] = 0.1;
            TH1D * hsyst = (TH1D *) finSyst->Get(Form("even_errors/even_%d_%d",cmin[i],cmax[i]));
            ysyst[j] = y[j] * hsyst->GetBinContent(1);
            hsyst->Delete();
        }
        N1EVENSUB3_syst[i] = new TGraphErrors(num, x, y, xerr, ysyst);
        N1EVENSUB3_syst[i]->SetLineWidth(2);
        N1EVENSUB3_syst[i]->SetLineColor(kBlue-10);
        N1EVENSUB3_syst[i]->SetFillColor(kBlue-10);
    }
    //--


    TCanvas * c = new TCanvas("c", "c", 1000, 600);
    c->Divide(2,1,0,0);
    TPad * pad1 = (TPad *) c->cd(1);
    pad1->SetTopMargin(0.07);
    h1 = new TH1D("h1", "", 100, -2.8, 2.8);
    h1->SetStats(0);
    h1->SetXTitle("#eta");
    h1->SetYTitle("v_{1}^{even}");
    h1->GetYaxis()->SetDecimals();
    h1->GetXaxis()->CenterTitle();
    h1->GetYaxis()->CenterTitle();
    h1->GetXaxis()->SetTitleOffset(1.15);
    h1->GetYaxis()->SetTitleOffset(1.65);
    h1->GetYaxis()->SetRangeUser(-0.016, 0.036);
    h1->Draw();
    for (int i = 0; i<=5; i++) {
        N1EVENSUB3_syst[i]->Draw("[]2");
    }
    for (int i = 0; i<=5; i++) {
        N1EVENSUB3[i]->Draw("p");
    }
    TBox * box0 = new TBox(-0.4, -0.013, 0.4, 0.02);
    box0->SetFillColor(kWhite);
    box0->SetFillStyle(1001);
    // box0->Draw("same");
    TLine * ln0 = new TLine(-2.8, 0.0, 2.8, 0.0);
    ln0->Draw();

    TPaveText * tx0 = new TPaveText(0.184, 0.947, 0.399, 0.986, "NDC");
    SetTPaveTxt(tx0, 20);
    tx0->AddText("#bf{CMS} #it{Preliminary},  v_{1}^{even}{#eta_{C} = #eta_{ROI}}");
    tx0->Draw();

    TLegend * leg1 = new TLegend(0.36, 0.58, 0.88, 0.88);
    SetLegend(leg1, 22);
    leg1->SetNColumns(2);
    for (int i = 0; i<ncbins; i++) {
        leg1->AddEntry(N1EVENSUB3[i],Form("%d-%d%%",cmin[i],cmax[i]),"p");
    }
    leg1->Draw();

    TPad * pad2 = (TPad *) c->cd(2);
    pad2->SetTopMargin(0.07);
    pad2->SetRightMargin(0.01);
    h2 = (TH1D *) h1->Clone("h2");
    h2->GetYaxis()->SetTitleSize(0.0);
    h2->GetYaxis()->SetLabelSize(0.0);
    h2->GetXaxis()->SetTitleSize(0.07);
    h2->GetXaxis()->SetTitleOffset(0.90);
    h2->GetXaxis()->SetLabelSize(0.06);
    h2->GetXaxis()->SetLabelOffset(0.00);
    h2->Draw();
    for (int i = 6; i<ncbins; i++) {
        N1EVENSUB3_syst[i]->Draw("[]2");
    }
    for (int i = 6; i<ncbins; i++) {
        N1EVENSUB3[i]->Draw("p");
    }
    TBox * box1 = new TBox(-0.4, -0.013, 0.4, 0.02);
    box1->SetFillColor(kWhite);
    box1->SetFillStyle(1001);
    //box1->Draw("same");
    TLine * ln1 = new TLine(-2.8, 0.0, 2.8, 0.0);
    ln1->Draw();

    TPaveText * tx1 = new TPaveText(0.001, 0.938, 0.219, 0.981, "NDC");
    SetTPaveTxt(tx1, 20);
    tx1->AddText("PbPb 5.02 TeV,  0.3 < p_{T} < 3.0 GeV/c");
    tx1->Draw();

    c->Print("../figures/fig5A.pdf","pdf");
    c->Print("../figures/fig5A.png","png");

}
