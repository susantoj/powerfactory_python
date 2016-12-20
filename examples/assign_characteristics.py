"""
################################
##   assign_characteristics.py 
################################
- Gets all characteristics in the characteristics folder
- Matches load names with characteristic names
- If there is a match, assign the characteristic to the load
- If there no match, print a warning
"""

import powerfactory as pf

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Operational library
oplib = app.GetProjectFolder('oplib')
# Characteristics
opchar = oplib.GetContents('Characteristics')[0][0]

# Create dictionary of loads classified by load local name
load_dict = {}
loads = app.GetCalcRelevantObjects('*.ElmLod')
for load in loads:
    load_dict[load.loc_name] = load

print_str('Assigning characteristics to loads...') 

# Get all characteristics in characteristics folder    
load_chars = opchar.GetContents('*.*')[0]

# Assign characteristics to loads
for char in load_chars:
    if char.loc_name in load_dict:
        load = load_dict[char.loc_name]
        pliniref = load.CreateObject('ChaRef','plini')
        pliniref[0].typ_id = char
        app.PrintPlain(load)
    else:
        app.PrintWarn('Load ' + str(char) + ' not found...')
