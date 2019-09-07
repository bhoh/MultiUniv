from CommonPyTools.python.CommonTools import *

###########################
# Number of Leptons and WP
###########################

#Nlep='2'
#eleWP='mediumSelectiveQ'

McWeight = 'evt_weight_total_gen * evt_weight_total_rec * electron_double_recoSF_passMediumID * electron_double_idSF_passMediumID * electron_double_recoSF_passMediumID * electron_double_trigSF_DoubleElectron_passMediumID * electron_double_extraTrigSF_passMediumID'
#McWeight = 'evt_weight_total_gen * evt_weight_total_rec'

#--------------------    
# MC
#--------------------    

samples['DYJets@DYJetsToEE'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'evt_tag_dielectron_gen == 1',
    'weight' :McWeight,
    }

samples['DYJets10to50@DYJets10to50ToEE'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'evt_tag_dielectron_gen == 1',
    'weight' :McWeight,
    }

samples['DYJets@DYJetsToTauTau'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'evt_tag_ditau_gen == 1',
    'weight' :McWeight,
    }

samples['DYJets10to50@DYJets10to50ToTauTau'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'evt_tag_ditau_gen == 1',
    'weight' :McWeight,
    }

samples['TTLL_powheg'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WJets_MG'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WW_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WZ_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['ZZ_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['DoubleEG'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :'1',
    }

#samples['DoubleMuon'] = {
#    'skim'   :'',
#    'weight' :'1',
#    }

#--------------------    
# DATA driven QCD
#--------------------
'''
samples['DoubleEG_FakeElEl'] = {
    'skim'   :'MetFt_L_v0_LL_v0_MuMuOrElElFake_v1', #TODO: this skim is not exist currently
    'weight' :'1',
    }

samples['DobuleMuon_FakeMuMu'] = {
    'skim'   :'MetFt_L_v0_LL_v0_MuMuOrElElFake_v1', #TODO: this skim is not exist currently
    'weight' :'1',
    }
'''
