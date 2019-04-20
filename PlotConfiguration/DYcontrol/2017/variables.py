from CommonPyTools.python.CommonTools import *

columns=['ALL'] # To read all
#columns=['diLep_Ch','diLep_m','diLep_pt','nPV']

# xaxis, yaxis to set title

variables['mll'] = {
    'name': 'diLep_m',
    'range':(120,50,120),
    'xaxis': 'm_{ll} [GeV]',
    'fold' : 3
    }
variables['ZpT'] = {
    'name': 'diLep_pt',
    'range':(120,0,120),
    'xaxis': 'Z_{pt} [GeV]',
    'fold' : 3
    }

variables['passSelectQ'] = {
    'name': 'diLep_passSelectiveQ',
    'range':(4,-1,3),
    'xaxis': 'passSelectQ',
    'fold' : 3
    }

variables['IdSF_Q_Up'] = {
    'name': 'IdSF_Q_Up',
    'range':(40,-1,1.5),
    'xaxis': 'IdSF_Q_Up',
    'fold' : 3
    }

variables['IdSF_Q_Do'] = {
    'name': 'IdSF_Q_Do',
    'range':(40,-1,1.5),
    'xaxis': 'IdSF_Q_Do',
    'fold' : 3
    }

variables['IdSF_Q'] = {
    'name': 'IdSF_Q',
    'range':(40,-1,1.5),
    'xaxis': 'IdSF_Q',
    'fold' : 3
    }
