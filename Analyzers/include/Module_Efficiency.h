#ifndef Module_Efficiency_h
#define Module_Efficiency_h

#include "AnalyzerCore.h"
#include "RootHelper.h"

class Module_Efficiency : public AnalyzerCore {

public:
  Module_Efficiency();
  ~Module_Efficiency();

  void initializeAnalyzer();
  void executeEventFromParameter(AnalyzerParameter param);
  void executeEvent();

  Event* evt;

  TTree *newtree;

  void WriteHist();

private:

  std::vector<Lepton*> leps;
  double Aod_pt[2], Aod_eta[2]; //TODO lets use vector later

  double trgSF;
  double trgSF_Up;
  double trgSF_Dn;

  double ElrecoSF, ElrecoSF_Up, ElrecoSF_Dn;
  double ElIdSF, ElIdSF_Up, ElIdSF_Dn;

  double MuIdSF, MuIdSF_Up, MuIdSF_Dn;
  double MuIsoSF, MuIsoSF_Up, MuIsoSF_Dn;

  double DiElrecoSF, DiElrecoSF_Up, DiElrecoSF_Dn;
  double DiElIdSF, DiElIdSF_Up, DiElIdSF_Dn;

  double DiMuIdSF, DiMuIdSF_Up, DiMuIdSF_Dn;
  double DiMuIsoSF, DiMuIsoSF_Up, DiMuIsoSF_Dn;

  double (MCCorrection::*LeptonID_SF)(TString,double,double,int);
  double (MCCorrection::*LeptonISO_SF)(TString,double,double,int);
  double (MCCorrection::*LeptonReco_SF)(double,double,int);

  std::vector<Muon> muons;
  std::vector<Electron> electrons;

  TString LeptonID_key;
  TString trgSF_key0, trgSF_key1;

  TString LeptonISO_key;


};



#endif
