#include "Muon.h"

ClassImp(Muon)

Muon::Muon() : Lepton() {
  j_chi2 = 999.;
  j_PFCH04 = -999.;
  j_PFNH04 = -999.;
  j_PFPH04 = -999.;
  j_PU04 = -999.;
  j_trkiso = -999.;
  this->SetLeptonFlavour(MUON);
  j_MiniAODPt = -999.;
  j_rc = -999.;
  j_rc_err = -999.;
  j_TunePPtError = -999.;

  j_relIsoNoPH = -999.;
  j_relIsoNoPHNoCH = -999.;
}

Muon::~Muon(){
}

void Muon::SetTypeBit(unsigned int typebit){
  j_TypeBit = typebit;
}

void Muon::SetIDBit(unsigned int idbit){
  j_IDBit = idbit;
}

void Muon::SetIso(double ch04, double nh04, double ph04, double pu04, double trkiso){
  j_PFCH04 = ch04;
  j_PFNH04 = nh04;
  j_PFPH04 = ph04;
  j_PU04 = pu04;
  j_trkiso = trkiso;
  CalcPFRelIso();
}

void Muon::SetRelIsoFSRStudy(){
  j_relIsoNoPH =     (j_PFCH04+std::max( 0., j_PFNH04 - 0.5*j_PU04 )) / this->Pt();
  j_relIsoNoPHNoCH = (std::max( 0., j_PFNH04 - 0.5*j_PU04 )) / this->Pt();
}

void Muon::SetChi2(double chi2){
  j_chi2 = chi2;
}

void Muon::CalcPFRelIso(){
  double absiso = j_PFCH04+std::max( 0., j_PFNH04 + j_PFPH04 - 0.5*j_PU04 );
  //cout << "[Muon::CalcPFRelIso] j_PFCH04 = " << j_PFCH04 << endl;
  //cout << "[Muon::CalcPFRelIso] j_PFNH04 = " << j_PFNH04 << endl;
  //cout << "[Muon::CalcPFRelIso] j_PFPH04 = " << j_PFPH04 << endl;
  //cout << "[Muon::CalcPFRelIso] j_PU04 = " << j_PU04 << endl;
  //cout << "[Muon::CalcPFRelIso] --> absiso = " << absiso << endl;
  this->SetRelIso(absiso/this->Pt());
  //this->SetRelIso(absiso/this->MiniAODPt()); //TODO This is same as IDBit
}

double Muon::EA(){

  double eta = fabs(this->Eta());

  if     (eta<0.8000) return 0.0566;
  else if(eta<1.3000) return 0.0562;
  else if(eta<2.0000) return 0.0363;
  else if(eta<2.2000) return 0.0119;
  else if(eta<2.4000) return 0.0064;
  else return 0.0064;

}

void Muon::SetMiniAODPt(double d){
  j_MiniAODPt = d;
}
void Muon::SetMiniAODTunePPt(double d){
  j_MiniAODTunePPt = d;
}

void Muon::SetTrackerLayersWithMeasurement(int trackerLayers){
   j_trackerLayers = trackerLayers;
}


void Muon::SetMomentumScaleAndError(double rc, double rc_err){
  j_rc = rc;
  j_rc_err = rc_err;
}

void Muon::SetTuneP4(double pt, double pt_err, double eta, double phi, double q){
  j_TuneP4.SetPtEtaPhiM(pt,eta,phi,M());
  j_TuneP4.SetCharge(q);
  j_TunePPtError = pt_err;
}

bool Muon::PassID(TString ID){
  //==== POG
  if(ID=="POGTight") return isPOGTight();
  if(ID=="POGHighPt") return isPOGHighPt();
  if(ID=="POGMedium") return isPOGMedium();
  if(ID=="POGLoose") return isPOGLoose();
  if(ID=="POGTightWithTightIso") return Pass_POGTightWithTightIso();
  if(ID=="POGLooseWithLooseIso") return Pass_POGLooseWithLooseIso();
  if(ID=="POGHighPtWithLooseTrkIso") return Pass_POGHighPtWithLooseTrkIso();
  //==== Customized
  if(ID=="POGTightWithRelIsoNoPH") return Pass_isPOGTightWithRelIsoNoPH();
  if(ID=="POGTightWithRelIsoNoPHCH") return Pass_isPOGTightWithRelIsoNoPHCH();
  if(ID=="POGTightWithLooseIso") return Pass_POGTightWithLooseIso();
  if(ID=="POGMediumWithLooseTrkIso") return Pass_POGMediumWithLooseTrkIso();
  if(ID=="HNLoose") return Pass_HNLoose();
  if(ID=="HNTight") return Pass_HNTight();
  if(ID=="TEST") return Pass_TESTID();

  cout << "[Electron::PassID] No id : " << ID << endl;
  exit(EXIT_FAILURE);

  return false;

}

bool Muon::isPOGTightIso(){
  if(!( RelIso()<0.15 ))  return false;
  return true;
}

bool Muon::isAntiIso(int syst){
  double reliso = RelIso();
  double reliso_min=0.17; //TODO: need discussion
  double reliso_max=0.25;

  if(syst==0){ }
  else if(syst==1){ reliso_min = 0.18; }//TODO: need discussion
  else if(syst==-1){ reliso_min = 0.16; }//TODO: need discussion
  else{
    cout << "[Muon::isAntiIso] No syst flag : " << syst << endl;
    exit(EXIT_FAILURE);
    return false;
  }

  if(!(reliso>reliso_min && reliso<reliso_max)) return false;
  return true;
}

bool Muon::Pass_isPOGTightWithRelIsoNoPH(){
  if(!( isPOGTight() )) return false;
  if(!( j_relIsoNoPH < 0.15 ))  return false;
  return true;
}

bool Muon::Pass_isPOGTightWithRelIsoNoPHCH(){
  if(!( isPOGTight() )) return false;
  if(!( j_relIsoNoPHNoCH < 0.15 ))  return false;
  return true;
}

bool Muon::Pass_POGTightWithTightIso(){
  if(!( isPOGTight() )) return false;
  if(!( RelIso()<0.15 ))  return false;
  return true;
}

bool Muon::Pass_POGTightWithLooseIso(){
  if(!( isPOGTight() )) return false;
  if(!( RelIso()<0.25 ))  return false;
  return true;
}

bool Muon::Pass_POGLooseWithLooseIso(){
  if(!( isPOGLoose() )) return false;
  if(!( RelIso()<0.25 ))  return false;
  return true;
}

bool Muon::Pass_POGHighPtWithLooseTrkIso(){
  if(!( isPOGHighPt() )) return false;
  if(!( TrkIso()/TuneP4().Pt()<0.1 )) return false;
  return true;
}

bool Muon::Pass_POGMediumWithLooseTrkIso(){
  if(!( isPOGMedium() )) return false;
  if(!( TrkIso()/this->Pt()<0.1 )) return false;
  return true;
}

bool Muon::Pass_HNLoose() const{
  if(!( isPOGTight() )) return false;
  if(!( RelIso()<0.4 )) return false;
  return true;
}

bool Muon::Pass_HNTight() const{
  if(!( isPOGTight() )) return false;
  if(!( RelIso()<0.15 )) return false;
  return true;
}

//==== TEST ID

bool Muon::Pass_TESTID(){
  return true;
}
