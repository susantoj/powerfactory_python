"""
############################
##   project_folders.py   
############################

Gets common project folders

"""
import powerfactory as pf

app = pf.GetApplication()

#########
# MODEL #
#########

# Network model
netmod = app.GetProjectFolder('netmod')

# Network data
netdata = app.GetProjectFolder('netdat')

# Diagrams
diag_fold = app.GetProjectFolder('dia')

# Variations
var_fold = app.GetProjectFolder('scheme')

###########
# LIBRARY #
###########

# Equipment library
equip = app.GetProjectFolder('equip')
lines_fold = equip.GetContents('Lines')[0][0]

# User defined models
main_lib = equip.GetParent()
udm = main_lib.GetContents('User Defined Models*')[0][0]

# Script library
script_lib = app.GetProjectFolder('script')

# Template library
templ_lib = app.GetProjectFolder('templ')

# Operational library
oplib = app.GetProjectFolder('oplib')

# Characteristics
opchar = oplib.GetContents('Characteristics')[0][0]

# Thermal ratings
therm_fold = app.GetProjectFolder('therm')

# MVAr limit curves
mvar_fold = app.GetProjectFolder('mvar')

##############
# STUDY CASE #
##############

# Study cases
op_scen = app.GetProjectFolder('scen')

# Operational scenarios
sc_fold = app.GetProjectFolder('study')
