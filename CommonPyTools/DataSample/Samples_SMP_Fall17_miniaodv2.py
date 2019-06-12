# alias PD xsec nmc sumw
#TODO: ttH_bb, ttH_nonbb, SingleTop samples, (QCD MuEnriched) to be added
sampleInfo = {
'DYJets10to50_MG'	: {'name': 'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8',	'xsec': 18610,		'nMC':39521230,		'Nsum': 39489654 },
'DYJets'		: {'name': 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',	'xsec': 6225.42,	'nMC':182359906,	'Nsum': 123584524 },
'TTJJ_powheg'		: {'name': 'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',			'xsec': 377.96,		'nMC':42357944,		'Nsum': 42357944 },
'TTLJ_powheg'		: {'name': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,		'nMC':111325048,	'Nsum': 110424244 },
'TTLL_powheg'		: {'name': 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',			'xsec': 88.29,		'nMC':8705576,		'Nsum': 8634992 },
'SingleTop_sch_top'              : {'name': 'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', 'xsec': 6.35, 'nMC':9883805, 'Nsum': 9883805 },
'SingleTop_tch_antitop'           : {'name': 'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'xsec': 80.95, 'nMC':3939990, 'Nsum':3939990 },
'SingleTop_tch_top'              : {'name': 'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'xsec':136.02, 'nMC':5865875, 'Nsum':5865875 },
'SingleTop_tW_top'             : {'name': 'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'xsec':35.85, 'nMC':7794186, 'Nsum': 7794186 },
'SingleTop_tW_antitop'          : {'name': 'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'xsec': 35.85, 'nMC':7977430, 'Nsum': 7977430 },
'ttH_bb'            : {'name': 'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8', 'xsec': 0.2918466, 'nMC':8000000, 'Nsum': 8000000 },
'ttH_nonbb'         : {'name': 'ttHNonTobb_M125_TuneCP5_13TeV-powheg-pythia8', 'xsec': 0.2151, 'nMC':7669336, 'Nsum': 7669336 },
'WJets_MG'		: {'name': 'WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8',		'xsec': 61526.7,	'nMC':77700506,		'Nsum': 77631180 },
'WW_pythia'		: {'name': 'WW_TuneCP5_13TeV-pythia8',					'xsec': 118.7,		'nMC':7791498,		'Nsum': 7791498 },
'WZ_pythia'		: {'name': 'WZ_TuneCP5_13TeV-pythia8',					'xsec': 47.13,		'nMC':3928630,		'Nsum': 3928630 },
'ZZ_pythia'		: {'name': 'ZZ_TuneCP5_13TeV-pythia8',					'xsec': 16.523,		'nMC':1949768,		'Nsum': 1949768 },
'ttW'			: {'name': 'ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8',			'xsec': 0.61,		'nMC':9425384,		'Nsum': 9384328 },
'ttZ'			: {'name': 'ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8',			'xsec': 0.780,		'nMC':9698473,		'Nsum': 9678691 },


'CHToCB_M020'		:{'name' :'ChargedHiggsToCB_M020_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M030'		:{'name' :'ChargedHiggsToCB_M030_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M040'		:{'name' :'ChargedHiggsToCB_M040_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':264000,	'Nsum': 264000 },
'CHToCB_M050'		:{'name' :'ChargedHiggsToCB_M050_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':292000,	'Nsum': 292000 },
'CHToCB_M060'		:{'name' :'ChargedHiggsToCB_M060_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M070'		:{'name' :'ChargedHiggsToCB_M070_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M075'		:{'name' :'ChargedHiggsToCB_M075_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':53000,	'Nsum': 53000 },
'CHToCB_M085'		:{'name' :'ChargedHiggsToCB_M085_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M090'		:{'name' :'ChargedHiggsToCB_M090_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M100'		:{'name' :'ChargedHiggsToCB_M100_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':292000,	'Nsum': 292000 },
'CHToCB_M110'		:{'name' :'ChargedHiggsToCB_M110_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M120'		:{'name' :'ChargedHiggsToCB_M120_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':292000,	'Nsum': 292000 },
'CHToCB_M130'		:{'name' :'ChargedHiggsToCB_M130_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },
'CHToCB_M140'		:{'name' :'ChargedHiggsToCB_M140_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':292000,	'Nsum': 292000 },
'CHToCB_M160'		:{'name' :'ChargedHiggsToCB_M160_TuneCP5_PSweights_13TeV-madgraph-pythia8',	'xsec': 365.34,	'nMC':300000,	'Nsum': 300000 },

'TT_MG'		:{'name' :'TTJets_TuneCP5_13TeV-madgraphMLM-pythia8',	'xsec': 831.59,	'nMC':8026103,	'Nsum': 8026103 },
'ttbb'		:{'name' :'ttbb_4FS_ckm_NNPDF31_TuneCP5_amcatnlo_madspin_pythia',	'xsec': 0.6,	'nMC':5993190,	'Nsum': 5993190 },
'TTLJ_powheg_Do'		:{'name' :'TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':27104055,	'Nsum': 27104055 },
'TTLJ_powheg_Up'		:{'name' :'TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':26166070,	'Nsum': 26166070 },
'TTLJ_powheg_hdamp_Do'		:{'name' :'TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':26367765,	'Nsum': 26367765 },
'TTLJ_powheg_hdamp_Up'		:{'name' :'TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':27191508,	'Nsum': 27191508 },
'TTLJ_powheg_mass_Do'		:{'name' :'TTToSemiLeptonic_mtop171p5_TuneCP5_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':24357098,	'Nsum': 24357098 },
'TTLJ_powheg_mass_Up'		:{'name' :'TTToSemiLeptonic_mtop173p5_TuneCP5_PSweights_13TeV-powheg-pythia8',	'xsec': 365.34,	'nMC':22528538,	'Nsum': 22528538 },

}
