from CommonPyTools.python.CommonTools import *
SKFlat_WD = os.getenv('SKFlat_WD')
sys.path.insert(0,SKFlat_WD+'/CommonTools/include') 
from Definitions import *

# supercut will be applied last in the cuts
supercut = 'evt_tag_dimuon_gen == 1'

cuts['full_phase'] = 'evt_tag_dimuon_gen == 1 && evt_tag_dimuon_fiducial_post_fsr == 1 '
cuts['full_phase_dRp1'] = 'evt_tag_dimuon_gen == 1 && evt_tag_dimuon_fiducial_lepton_matched_dressed_drX[0] == 1 '

