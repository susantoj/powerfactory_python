"""
############################
##   element_dictionaries.py   
############################

- Gets lists of buses, generators and lines
- Creates dictionaries for each element type with the object name as the key

"""

import powerfactory as pf

app = pf.GetApplication()
app.ClearOutputWindow()

# Create dictionary of buses
bus_dict = {}
buses = app.GetCalcRelevantObjects('*.ElmTerm')
for bus in buses:
    bus_dict[bus.loc_name] = bus
    
# Create dictionary of lines 
line_dict = {}
lines = app.GetCalcRelevantObjects('*.ElmLne')
for line in lines:
    line_dict[line.loc_name] = line    
    
# Create dictionary of synchronous generators 
gen_dict = {}
gens = app.GetCalcRelevantObjects('*.ElmSym')
for gen in gens:
    gen_dict[gen.loc_name] = gen

# Loop through generator dictionary and print key and generator object
for gen_key in gen_dict.keys():
    app.PrintPlain(gen_key)
    app.PrintPlain(gen_dict[gen_key])
