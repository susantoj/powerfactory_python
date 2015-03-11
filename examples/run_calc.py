"""
############################
##   run_calc.py   
############################

- Gets a short circuit object from the active study case
- Set up the short circuit case (IEC 3-phase fault on all busbars)
- Runs the short circuit calculation

"""

import powerfactory as pf

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Get short circuit calculation object
shc = app.GetFromStudyCase('ComShc')

# Set up short circuit calculation
shc.iopt_mde = 1    # IEC fault mode
iopt_allbus = 2     # All busbars

# Run short circuit calculation
ierr = shc.Execute()
