#sys.path.insert(0,'./')
#structure={}
#import  structure

try:
  #mc =[skey for skey in samples if skey not in ['SingleMuon', 'SingleElectron'] and not skey.startswith('Fake')]
  mc = [skey for skey in groupPlot if skey not in ['DATA','SingleMuon', 'SingleElectron'] and not skey.startswith('Fake')]
  mc = mc + [skey for skey in plot if skey not in ['DATA','SingleMuon', 'SingleElectron'] and not skey.startswith('Fake')]
except NameError:
  mc =[]

print 'nuisances: mc:',mc

nuisances['lumi'] = {
    'name' : 'lumi_13TeV',
    'type' : 'lnN',
    'samples' : dict((skey, '1.023') for skey in mc)
}

nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
   #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
   #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}
#
#nuisances['ttxsec'] = {
#    'name' : 'ttxsec',
#    'type' : 'lnN',
#    'samples' : {
#      'TTLJ_powheg'	: '1.06114',
#      'TTLL_powheg'	: '1.06114',
#      'TTJJ_powheg'	: '1.06114',
#    }
#}
#
#nuisances['JES'] = {
#    'name' : 'JES',
#    'kind' : 'variableChange',
#    'type' : 'shape',
#    'samples' : { 
#      'DYJet'                 : ['1', '1'],
#      'DYJets10to50_MG'       : ['1', '1'],
#      'WJets_MG'              : ['1', '1'],
#      'TTLJ_powheg'	      : ['1', '1'],
#      'TTLL_powheg'	      : ['1', '1'],
#      'TTJJ_powheg'	      : ['1', '1'],
#      'SingleTop_sch_top'     : ['1', '1'],
#      'SingleTop_tch_top'     : ['1', '1'],
#      'SingleTop_tch_antitop' : ['1', '1'],
#      'SingleTop_tW_top'      : ['1', '1'],
#      'SingleTop_tW_antitop'  : ['1', '1'],
#      'WW_pythia'             : ['1', '1'],
#      'WZ_pythia'             : ['1', '1'],
#      'ZZ_pythia'             : ['1', '1'],
#      'ttW'                   : ['1', '1'],
#      'ttZ'                   : ['1', '1'],
#      'ttH_bb'                : ['1', '1'],
#      'ttbb'                  : ['1', '1'],
#    },
#    'variablesUp' : {
#	'fitted_dijet_mass' : [
#          'fitted_dijet_mass_JES_Up',
#	  'fitted_dijet_m_JES_Up'
#	],
#	#'fitter_status' : [
#	#  'fitter_status_JES_Up',
#	#  'fitter_status_JES_Up'
#	#],
#	#'1st_leading_jet_pt' : [
#	#  '1st_leading_jet_pt_JES_Up',
#	#  'selected_jet_pt_JES_Up[0]'
#	#],
#	#'2nd_leading_jet_pt' : [
#	#  '2nd_leading_jet_pt_JES_Up',
#	#  'selected_jet_pt_JES_Up[1]'
#        #],
#	#'3rd_leading_jet_pt' : [
#	#  '3rd_leading_jet_pt_JES_Up',
#	#  'selected_jet_pt_JES_Up[2]'
#        #],
#	#'4th_leading_jet_pt' : [
#	#  '4th_leading_jet_pt_JES_Up',
#	#  'selected_jet_pt_JES_Up[3]',
#        #],
#	#'njets' : [
#	#  'njets_JES_Up',
#	#  'njets_JES_Up'
#	#],
#	#'MET' : [
#	#  'MET_JES_Up',
#	#  'MET_JES_Up'
#	#],
#    },
#    'variablesDo' : {
#	'fitted_dijet_mass' : [
#          'fitted_dijet_mass_JES_Do',
#	  'fitted_dijet_m_JES_Do'
#	],
#	#'fitter_status' : [
#	#  'fitter_status_JES_Do',
#	#  'fitter_status_JES_Do'
#	#],
#	#'1st_leading_jet_pt' : [
#	#  '1st_leading_jet_pt_JES_Do',
#	#  'selected_jet_pt_JES_Do[0]'
#	#],
#	#'2nd_leading_jet_pt' : [
#	#  '2nd_leading_jet_pt_JES_Do',
#	#  'selected_jet_pt_JES_Do[1]'
#        #],
#	#'3rd_leading_jet_pt' : [
#	#  '3rd_leading_jet_pt_JES_Do',
#	#  'selected_jet_pt_JES_Do[2]'
#        #],
#	#'4th_leading_jet_pt' : [
#	#  '4th_leading_jet_pt_JES_Do',
#	#  'selected_jet_pt_JES_Do[3]',
#        #],
#	#'njets' : [
#	#  'njets_JES_Do',
#	#  'njets_JES_Do'
#	#],
#	#'MET' : [
#	#  'MET_JES_Do',
#	#  'MET_JES_Do'
#	#],
#    },
#}
#
#nuisances['ttxsec'] = {
#    'name' : 'ttxsec',
#    'type' : 'lnN',
#    'samples' : {
#      'TTLJ_powheg'	: '1.06114',
#      'TTLL_powheg'	: '1.06114',
#      'TTJJ_powheg'	: '1.06114',
#    }
#}
#
#nuisances['JES'] = {
#    'name' : 'JES',
#    'kind' : 'variableChange',
#    'type' : 'shape',
#    'samples' : { 
#      'DYJet'                 : ['1', '1'],
#      'DYJets10to50_MG'       : ['1', '1'],
#      'WJets_MG'              : ['1', '1'],
#      'TTLJ_powheg'	      : ['1', '1'],
#      'TTLL_powheg'	      : ['1', '1'],
#      'TTJJ_powheg'	      : ['1', '1'],
#      'SingleTop_sch_top'     : ['1', '1'],
#      'SingleTop_tch_top'     : ['1', '1'],
#      'SingleTop_tch_antitop' : ['1', '1'],
#      'SingleTop_tW_top'      : ['1', '1'],
#      'SingleTop_tW_antitop'  : ['1', '1'],
#      'WW_pythia'             : ['1', '1'],
#      'WZ_pythia'             : ['1', '1'],
#      'ZZ_pythia'             : ['1', '1'],
#      'ttW'                   : ['1', '1'],
#      'ttZ'                   : ['1', '1'],
#      'ttH_bb'                : ['1', '1'],
#      'ttbb'                  : ['1', '1'],
#    },
#    'variablesUp' : {
#	'fitted_dijet_mass' : [
#         'fitted_dijet_mass_JES_Up',
#	 'fitted_dijet_m_JES_Up'
#	],
#	'fitter_status' : [
#	  'fitter_status_JES_Up',
#	  'fitter_status_JES_Up'
#	],
#	'1st_leading_jet_pt' : [
#	  '1st_leading_jet_pt_JES_Up',
#	  'selected_jet_pt_JES_Up[0]'
#	],
#	'2nd_leading_jet_pt' : [
#	  '2nd_leading_jet_pt_JES_Up',
#	  'selected_jet_pt_JES_Up[1]'
#        ],
#	'3rd_leading_jet_pt' : [
#	  '3rd_leading_jet_pt_JES_Up',
#	  'selected_jet_pt_JES_Up[2]'
#        ],
#	'4th_leading_jet_pt' : [
#	  '4th_leading_jet_pt_JES_Up',
#	  'selected_jet_pt_JES_Up[3]',
#        ],
#	'njets' : [
#	  'njets_JES_Up',
#	  'njets_JES_Up'
#	],
#	'MET' : [
#	  'MET_JES_Up',
#	  'MET_JES_Up'
#	],
#    },
#    'variablesDo' : {
#	'fitted_dijet_mass' : [
#          'fitted_dijet_mass_JES_Do',
#	  'fitted_dijet_m_JES_Do'
#	],
#	'fitter_status' : [
#	  'fitter_status_JES_Do',
#	  'fitter_status_JES_Do'
#	],
#	'1st_leading_jet_pt' : [
#	  '1st_leading_jet_pt_JES_Do',
#	  'selected_jet_pt_JES_Do[0]'
#	],
#	'2nd_leading_jet_pt' : [
#	  '2nd_leading_jet_pt_JES_Do',
#	  'selected_jet_pt_JES_Do[1]'
#        ],
#	'3rd_leading_jet_pt' : [
#	  '3rd_leading_jet_pt_JES_Do',
#	  'selected_jet_pt_JES_Do[2]'
#        ],
#	'4th_leading_jet_pt' : [
#	  '4th_leading_jet_pt_JES_Do',
#	  'selected_jet_pt_JES_Do[3]',
#        ],
#	'njets' : [
#	  'njets_JES_Do',
#	  'njets_JES_Do'
#	],
#	'MET' : [
#	  'MET_JES_Do',
#	  'MET_JES_Do'
#	],
#    },
#}
#nuisances['JER'] = {
#    'name' : 'JER',
#    'kind' : 'variableChange',
#    'type' : 'shape',
#    'samples' : {
#      'DYJet'                 : ['1', '1'],
#      'DYJets10to50_MG'       : ['1', '1'],
#      'WJets_MG'              : ['1', '1'],
#      'TTLJ_powheg'	      : ['1', '1'],
#      'TTLL_powheg'	      : ['1', '1'],
#      'TTJJ_powheg'	      : ['1', '1'],
#      'SingleTop_sch_top'     : ['1', '1'],
#      'SingleTop_tch_top'     : ['1', '1'],
#      'SingleTop_tch_antitop' : ['1', '1'],
#      'SingleTop_tW_top'      : ['1', '1'],
#      'SingleTop_tW_antitop'  : ['1', '1'],
#      'WW_pythia'             : ['1', '1'],
#      'WZ_pythia'             : ['1', '1'],
#      'ZZ_pythia'             : ['1', '1'],
#      'ttW'                   : ['1', '1'],
#      'ttZ'                   : ['1', '1'],
#      'ttH_bb'                : ['1', '1'],
#      'ttbb'                  : ['1', '1'],
#    },
#    'variablesUp' : {
#	'fitted_dijet_mass' : [
#          'fitted_dijet_mass_JER_Up',
#	  'fitted_dijet_m_JER_Up'
#	],
#	'fitter_status' : [
#	  'fitter_status_JER_Up',
#	  'fitter_status_JER_Up'
#	],
#	'1st_leading_jet_pt' : [
#	  '1st_leading_jet_pt_JER_Up',
#	  'selected_jet_pt_JER_Up[0]'
#	],
#	'2nd_leading_jet_pt' : [
#	  '2nd_leading_jet_pt_JER_Up',
#	  'selected_jet_pt_JER_Up[1]'
#        ],
#	'3rd_leading_jet_pt' : [
#	  '3rd_leading_jet_pt_JER_Up',
#	  'selected_jet_pt_JER_Up[2]'
#        ],
#	'4th_leading_jet_pt' : [
#	  '4th_leading_jet_pt_JER_Up',
#	  'selected_jet_pt_JER_Up[3]',
#        ],
#	'njets' : [
#	  'njets_JER_Up',
#	  'njets_JER_Up'
#	],
#	'MET' : [
#	  'MET_JER_Up',
#	  'MET_JER_Up'
#	],
#    },
#    'variablesDo' : {
#	'fitted_dijet_mass' : [
#          'fitted_dijet_mass_JER_Do',
#	  'fitted_dijet_m_JER_Do'
#	],
#	'fitter_status' : [
#	  'fitter_status_JER_Do',
#	  'fitter_status_JER_Do'
#	],
#	'1st_leading_jet_pt' : [
#	  '1st_leading_jet_pt_JER_Do',
#	  'selected_jet_pt_JER_Do[0]'
#	],
#	'2nd_leading_jet_pt' : [
#	  '2nd_leading_jet_pt_JER_Do',
#	  'selected_jet_pt_JER_Do[1]'
#        ],
#	'3rd_leading_jet_pt' : [
#	  '3rd_leading_jet_pt_JER_Do',
#	  'selected_jet_pt_JER_Do[2]'
#        ],
#	'4th_leading_jet_pt' : [
#	  '4th_leading_jet_pt_JER_Do',
#	  'selected_jet_pt_JER_Do[3]',
#        ],
#	'njets' : [
#	  'njets_JER_Do',
#	  'njets_JER_Do'
#	],
#	'MET' : [
#	  'MET_JER_Do',
#	  'MET_JER_Do'
#	],
#    },
#}
#

#nuisances['top_mass'] = {
#    'name' : 'top_mass',
#    'kind' : 'sampleChange',
#    'type' : 'shape',
#    'samples' : {
#      'TTLJ_powheg'	: ['1.','1.'],
#      'TTLL_powheg'	: ['1.','1.'],
#      'TTJJ_powheg'	: ['1.','1.'],
#    },
#    'samplesUp' : {
#      'TTLJ_powheg'	: 'TTLJ_powheg_mass_Up',
#      'TTLL_powheg'	: 'TTLL_powheg_mass_Up',
#      'TTJJ_powheg'    : 'TTJJ_powheg' #TODO add TTJJ_powheg_mass_Up sample later
#    },
#    'samplesDo' : {
#      'TTLJ_powheg'	: 'TTLJ_powheg', #TODO will add this sample
#      'TTLL_powheg'	: 'TTLL_powheg_mass_Do',
#      'TTJJ_powheg'	: 'TTJJ_powheg_mass_Do',
#    },
#}
#
#nuisances['TuneCP5'] = {
#    'name' : 'TuneCP5',
#    'kind' : 'sampleChange',
#    'type' : 'shape',
#    'samples' : {
#      'TTLJ_powheg'	: ['1.','1.'],
#      'TTLL_powheg'	: ['1.','1.'],
#      'TTJJ_powheg'	: ['1.','1.'],
#    },
#    'samplesUp' : {
#      'TTLJ_powheg'	: 'TTLJ_powheg_Up',
#      'TTLL_powheg'	: 'TTLL_powheg_Up',
#      'TTJJ_powheg'	: 'TTJJ_powheg_Up',
#    },
#    'samplesDo' : {
#      'TTLJ_powheg'	: 'TTLJ_powheg_Do',
#      'TTLL_powheg'	: 'TTLL_powheg_Do',
#      'TTJJ_powheg'	: 'TTJJ_powheg_Do',
#    },
#}
#
#nuisances['hdamp'] = {
#    'name' : 'hdamp',
#    'kind' : 'sampleChange',
#    'type' : 'shape',
#    'samples' : {
#      'TTLJ_powheg'	: ['1.','1.'],
#      'TTLL_powheg'	: ['1.','1.'],
#      'TTJJ_powheg'	: ['1.','1.'],
#    },
#    'samplesUp'   : { 
#      'TTLJ_powheg'	: 'TTLJ_powheg_hdamp_Up',
#      'TTLL_powheg'	: 'TTLL_powheg_hdamp_Up',
#      'TTJJ_powheg'	: 'TTJJ_powheg_hdamp_Up',
#    },
#    'samplesDo'   : {
#      'TTLJ_powheg'	: 'TTLJ_powheg_hdamp_Do',
#      'TTLL_powheg'	: 'TTLL_powheg_hdamp_Do',
#      'TTJJ_powheg'	: 'TTJJ_powheg_hdamp_Do',
#    },
#}
#
#nuisances['generator'] = {
#    'name' : 'generator',
#    'kind' : 'sampleChange',
#    'type' : 'shape',
#    'samples' : {
#      'TTLJ_powheg'	: ['1.','1.'],
#      'TTLL_powheg'	: ['0.','1.'],
#      'TTJJ_powheg'	: ['0.','1.'],
#    },
#    'samplesUp'   : {
#      'TTLJ_powheg'	: 'TT_MG',
#      'TTLL_powheg'	: 'zeros',
#      'TTJJ_powheg'	: 'zeros',
#    },
#    'samplesDo' : {
#      'TTLJ_powheg'	: 'TTLJ_powheg',
#      'TTLL_powheg'	: 'TTLL_powheg',
#      'TTJJ_powheg'	: 'TTJJ_powheg',
#    },
#    #TODO will add signal samples
#}
#
#nuisances['PUweight'] = {
#    'name' :'PUweight',
#    'kind' : 'weight',
#    'type' : 'shape',
#    'samples' : {
#      'DYJet'                 : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'DYJets10to50_MG'       : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'WJets_MG'              : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'TTLJ_powheg'	      : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'TTLL_powheg'	      : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'TTJJ_powheg'	      : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'SingleTop_sch_top'     : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'SingleTop_tch_top'     : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'SingleTop_tch_antitop' : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'SingleTop_tW_top'      : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'SingleTop_tW_antitop'  : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'WW_pythia'             : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'WZ_pythia'             : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'ZZ_pythia'             : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'ttW'                   : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'ttZ'                   : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'ttH_bb'                : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#      'ttbb'                  : ['PUweight_Up/PUweight', 'PUweight_Do/PUweight'],
#
#    }
#}
#
#nuisances['IdSF'] = {
#    'name' : 'IdSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'DYJets'	              : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'DYJets10to50_MG'       : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'WJets_MG'              : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'TTLJ_powheg'	      : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'TTLL_powheg'	      : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'TTJJ_powheg'	      : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'SingleTop_sch_top'         : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'SingleTop_tch_top'     : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'SingleTop_tch_antitop' : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'SingleTop_tW_top'      : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'SingleTop_tW_antitop'  : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'WW_pythia'             : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'WZ_pythia'             : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'ZZ_pythia'             : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'ttW'                   : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'ttZ'                   : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'ttH_bb'                : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#      'ttbb'                  : ['IdSF_Up/IdSF', 'IdSF_Do/IdSF'],
#    }
#}
#
#nuisances['IsoSF'] = {
#    'name' : 'IsoSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'DYJets'	              : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'DYJets10to50_MG'       : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'WJets_MG'              : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'TTLJ_powheg'	      : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'TTLL_powheg'	      : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'TTJJ_powheg'	      : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'SingleTop_sch_top'     : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'SingleTop_tch_top'     : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'SingleTop_tch_antitop' : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'SingleTop_tW_top'      : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'SingleTop_tW_antitop'  : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'WW_pythia'             : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'WZ_pythia'             : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'ZZ_pythia'             : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'ttW'                   : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'ttZ'                   : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'ttH_bb'                : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#      'ttbb'                  : ['IsoSF_Up/IsoSF', 'IsoSF_Do/IsoSF'],
#    }
#}
#
#nuisances['recoSF'] = {
#    'name' : 'recoSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'DYJets'	              : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'DYJets10to50_MG'       : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'WJets_MG'              : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'TTLJ_powheg'	      : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'TTLL_powheg'	      : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'TTJJ_powheg'	      : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'SingleTop_sch_top'     : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'SingleTop_tch_top'     : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'SingleTop_tch_antitop' : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'SingleTop_tW_top'      : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'SingleTop_tW_antitop'  : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'WW_pythia'             : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'WZ_pythia'             : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'ZZ_pythia'             : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'ttW'                   : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'ttZ'                   : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'ttH_bb'                : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#      'ttbb'                  : ['recoSF_Up/recoSF', 'recoSF_Do/recoSF'],
#    }
#}
#
#nuisances['trgSF'] = {
#    'name' : 'trgSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'DYJets'	              : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'DYJets10to50_MG'       : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'WJets_MG'              : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'TTLJ_powheg'	      : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'TTLL_powheg'	      : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'TTJJ_powheg'	      : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'SingleTop_sch_top'     : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'SingleTop_tch_top'     : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'SingleTop_tch_antitop' : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'SingleTop_tW_top'      : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'SingleTop_tW_antitop'  : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'WW_pythia'             : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'WZ_pythia'             : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'ZZ_pythia'             : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'ttW'                   : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'ttZ'                   : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'ttH_bb'                : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#      'ttbb'                  : ['trgSF_Up/trgSF', 'trgSF_Do/trgSF'],
#    }
#}
#
#
#nuisances['BTagSF'] = {
#    'name' : 'BTagSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'DYJets'	              : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'DYJets10to50_MG'       : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'WJets_MG'              : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'TTLJ_powheg'	      : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'TTLL_powheg'	      : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'TTJJ_powheg'	      : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'SingleTop_sch_top'     : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'SingleTop_tch_top'     : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'SingleTop_tch_antitop' : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'SingleTop_tW_top'      : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'SingleTop_tW_antitop'  : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'WW_pythia'             : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'WZ_pythia'             : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'ZZ_pythia'             : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'ttW'                   : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'ttZ'                   : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'ttH_bb'                : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#      'ttbb'                  : ['BTagSF_Up/BTagSF', 'BTagSF_Do/BTagSF'],
#    }
#}
#
'''
nuisances['MisTagSF'] = {
    'name' : 'MisTagSF',
    'kind'	: 'weight',
    'type'	: 'shape',
    'samples' : {
      'DYJets'	               : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'DYJets10to50_MG'       : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'WJets_MG'              : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'TTLJ_powheg'	       : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'TTLL_powheg'	       : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'TTJJ_powheg'	       : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'SingleTop_sch_top'     : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'SingleTop_tch_top'     : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'SingleTop_tch_antitop' : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'SingleTop_tW_top'      : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'SingleTop_tW_antitop'  : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'WW_pythia'             : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'WZ_pythia'             : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'ZZ_pythia'             : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'ttW'                   : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'ttZ'                   : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'ttH_bb'                : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
      'ttbb'                  : ['MisTagSF_Up/MisTagSF', 'MisTagSF_Do/MisTagSF'],
    }
}
'''

#nuisances['leptonSF'] = {
#    'name' : 'leptonSF',
#    'kind'	: 'weight',
#    'type'	: 'shape',
#    'samples' : {
#      'TTLJ_powheg'	: ['leptonSF_Up/leptonSF','leptonSF_Do/leptonSF'],
#      'TTLL_powheg'	: ['leptonSF_Up/leptonSF','leptonSF_Do/leptonSF'],
#      'TTJJ_powheg'	: ['leptonSF_Up/leptonSF','leptonSF_Do/leptonSF'],
#      }
#}
#
#nuisances['ttbbxsec'] = {
#    'name' : 'ttbbxsec',
#    'kind'	: 'weight', 
#    'type'	: 'shape',
#    'samples'   : {
#      'ttbb'	: ['2.05', '-0.05'],
#      }
#}
#
#nuisances['generator'] = {
#    'name' : 'generator',
#    'kind'	: 'weight', # Down is the same as nominal, nuisance for Signal sample
#    'type'	: 'shape',
#    'samples' : {
#      'CHToCB_M090'	: ['generator','1'],
#      'CHToCB_M100'	: ['generator','1'],
#      'CHToCB_M110'	: ['generator','1'],
#      }
#}

'''
nuisances['gentoppt_reweight'] = {
    'name' : 'gentoppt_reweight',
    'kind'	: 'weight', # Down is the same as nominal
    'type'	: 'shape',
    'samples' : {
      'TTLJ_powheg'	: ['gentoppt_reweight' , '1.'],
      'TTLL_powheg'	: ['gentoppt_reweight' , '1.'],
      'TTJJ_powheg'	: ['gentoppt_reweight' , '1.'],
      }
}
'''
## other systematics(JEC/JER/top_mass/MEtoPS/generator) are not defined as event-by-event weight

########## Efficiency and Energy Scale
#alphaS_syst  = ['PDFWeights_AlphaS[0]', 'PDFWeights_AlphaS[1]']
#id_syst_ele = ['LepSF'+Nlep+'l_ele_'+eleWP+'_Up', 'LepSF'+Nlep+'l_ele_'+eleWP+'_Do']

nuisances['alphaS'] = {
    'name'	: 'alphaS',
    'kind'	: 'PDF',
    'type'	: 'shape',
    'samples' : dict((skey, 'PDFWeights_AlphaS') for skey in mc)
}

nuisances['PDFError'] = {
    'name'	: 'pdfHESSIAN',
    'kind'	: 'PDF',
    'type'	: 'shape',
    'samples' : dict((skey, 'PDFWeights_Error') for skey in mc)
}
nuisances['PDfScale'] = {
    'name'	: 'pdfScale',
    'kind'	: 'PDF',
    'type'	: 'shape',
    'samples' : dict((skey, 'PDFWeights_Scale') for skey in mc)
}

