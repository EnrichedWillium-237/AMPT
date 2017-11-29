#include "TFile.h"
#include "TTree.h"
#include "iostream"
#include "vector"

void readTree()
{
	TFile * f = new TFile("tree.root");

	TTree * trPart = (TTree*) f->Get("QWTreeMaker/trV");
	TTree * trHep  = (TTree*) f->Get("QWHepMCMaker/trV");
	trPart->SetMakeClass(1);
	trHep->SetMakeClass(1);

	trPart->AddFriend(trHep);

	double b;

	vector<double>  *phi = 0;
	vector<double>  *eta = 0;
	vector<double>  *pt = 0;
	vector<double>  *charge = 0;

	trHep->SetBranchAddress("b", &b );
	trPart->SetBranchAddress("phi", &phi );
	trPart->SetBranchAddress("eta", &eta);
	trPart->SetBranchAddress("pt", &pt );
	trPart->SetBranchAddress("charge", &charge);



	std::cout << " !!! " << __LINE__ << " " << trPart->GetEntries() << std::endl;
	int ievt = 0; 
	while ( trPart->GetEntry(ievt++) )
	{
		std::cout << " b = " << b << "\t phi->size() = " << phi->size() << std::endl;
//		for ( auto it = phi->begin(); it != phi->end(); it++ ) {
//			std::cout << *it << std::endl;
//		}
		for ( unsigned int i = 0; i < phi->size(); i++ ) {
//			std::cout << "phi["<< i << "] = " << (*phi)[i] << std::endl;
		}
	}
}
