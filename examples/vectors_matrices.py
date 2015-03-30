"""
############################
##   vectors_matrices.py   
############################

- Creates a vector and matrix object in the active study case
- Puts dummy data into the vector and matrix objects
- Gets the data out of the matrix object, modifies an entry and puts it back into the matrix object

"""

import powerfactory as pf

# Get PowerFactory application
app = pf.GetApplication()
app.ClearOutputWindow()

# Get current study case
study = app.GetActiveStudyCase()

# Create PowerFactory vector and matrix objects
vec = study.CreateObject('IntVec')[0]
mat = study.CreateObject('IntMat')[0]

# Print out objects
app.PrintPlain(vec)
app.PrintPlain(mat)

# Generate dummy data for vector and matrix
# Note that vector data is a list and matrix data is a list of lists
vec_data = [1, 6, 8, 1, 5, 8]
mat_data = [[5, 7, 3], [2, 4, 6], [6, 1, 0]]

# Put dummy data into PowerFactory vector and matrix objects
vec.SetAttribute('V', vec_data)
mat.SetAttribute('M', mat_data)

# Get data from matrix object and print it out
data = mat.GetAttribute('M')
app.PrintPlain(data)

# Modify the (3,3) entry of the matrix
data[2][2] = 10

# Put modified data back into matrix
mat.SetAttribute('M', data)
