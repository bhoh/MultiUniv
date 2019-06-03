from CommonPyTools.python.CommonTools import *

###########################
# Number of Leptons and WP
###########################

#Nlep='1'
#eleWP='mediumSelectiveQ'

#XXX: diff. between IdSF and IdSF_Q ?
McWeight = 'baseW*PUweight*trgSF*recoSF*IdSF*IsoSF*recoSF*BTagSF*MisTagSF'
#McWeight = 'baseW*PUweight*trgSF*recoSF*IdSF*IsoSF*ZPtCor'

#--------------------    
# MC
#--------------------    

samples['DYJets'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'weight' :McWeight,
    }

samples['DYJets10to50_MG'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['WJets_MG'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['TTLJ_powheg'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['TTLL_powheg'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['TTJJ_powheg'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['SingleTop_sch_top'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['SingleTop_tch_top'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['SingleTop_tch_antitop'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['SingleTop_tW_top'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['SingleTop_tW_antitop'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['WW_pythia'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['WZ_pythia'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['ZZ_pythia'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

samples['ttW'] = {
    'skim'   :'',
    'weight' :McWeight,
    }
samples['ttZ'] = {
    'skim'   :'',
    'weight' :McWeight,
    }

#--------------------    
# DATA
#--------------------    
samples['SingleElectron'] = {
    'skim'   :'',
    'weight' :'1',
    }

samples['SingleMuon'] = {
    'skim'   :'',
    'weight' :'1',
    }