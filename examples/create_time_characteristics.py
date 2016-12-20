
"""
#####################################
##   create_time_characteristics.py   
#####################################
- Open a CSV file of 30min daily load profiles using TKinter file dialog box (for example "load_file.csv")
- Read CSV file and build list of loads
- Loop through list of loads and create time characteristics

Format of CSV file:
- Column 1:     Name of load
- Column 2-49:  Load demand (in kW) for each half hour interval from 0:00 to 23:30
"""

import tkinter as tk
from tkinter import filedialog
import sys
import csv
import powerfactory as pf

# Load object class definition
class csv_load():
    def __init__ (self, input):
        self.name = input[0]
        self.P = [float(i)/1000 for i in input[1:49]]   # Convert loads from kW to MW

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Operational library folder
oplib = app.GetProjectFolder('oplib')
# Characteristics folder
opchar = oplib.GetContents('Characteristics')[0][0]

# Select csv file
if len(sys.argv)>1:
    file_name_ = str(sys.argv[1])
else:
    root = tk.Tk()
    root.withdraw()
    file_name_ = filedialog.askopenfilename(title='Select a CSV file to open',filetypes=[('Comma Separated Value file', '*.csv')])
# Handler for cancel button
    if not file_name_:
        print_str('Script execution cancelled...')    
        exit()

# Read in lines from CSV file and put them into list of load objects
csv_loads = []        
with open(file_name_, 'r') as csvfile:
    line_file = csv.reader (csvfile, delimiter=",", quoting=csv.QUOTE_NONE)
    for row in line_file:
        csv_loads.append(csv_load(row))  

# Loop through each load in list
for load in csv_loads:
    # Create time characteristic
    app.PrintPlain('Creating time characteristic ' + load.name + '...')
    
    char = opchar.CreateObject('ChaTime', load.name)[0]        
    # Set up characteristic
    char.source = 0       # Data Source = Table
    char.repeat = 0       # Recurrence = Daily
    char.cunit = 0        # Resolution = Minutes
    char.stepSize = 30    # Step Size = Half hourly intervals
    char.usage = 2        # Usage = Absolute
    char.approx = 4       # Approximation = Hermite

    # Populate characteristic with load data
    char.SetAttribute('vector', load.P)
        
