"""
############################
##   results.py   
############################

- Runs a load flow
- Gets basic results from buses (voltage) and lines (loading)

"""

import powerfactory as pf

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Run load flow
ldf = app.GetFromStudyCase('ComLdf')
ierr = ldf.Execute()

# Get lists of buses and lines
buses = app.GetCalcRelevantObjects('*.ElmTerm')
lines = app.GetCalcRelevantObjects('*.ElmLne')

# Print bus voltages
for bus in buses:
    # Only consider busbars (iUsage = 0) and in-service buses
    if bus.iUsage == 0 and bus.outserv == 0:
        bus_v = round(bus.GetAttribute('m:u'),2)
        app.PrintPlain('Voltage on bus ' + str(bus) + ': ' + str(bus_v) + 'pu')
        
# Print loading on lines
for line in lines:
    if line.outserv == 0:
        loading = round(line.GetAttribute('m:loading'),2)
        app.PrintPlain('Loading on line ' + str(line) + ': ' + str(loading) + '%%')
