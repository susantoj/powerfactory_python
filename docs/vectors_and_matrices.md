## Accessing and manipulating vectors and matrices

One-dimensional (vector) and two-dimensional (matrix) data can be used in a variety of ways in PowerFactory, for example:

* Reactive power capability curves (matrix)
* Characteristics (vector and matrix)
* Thermal ratings (vector and matrix)
* Tower types (matrix)

Retrieving and setting vector and matrix data via Python is done by the `GetAttribute` and `SetAttribute` functions that is inherited from the base PowerFactory dataobject class.

***Important note***: PowerFactory vector and matrices are represented in Python as lists and lists of lists respectively.

## Retrieving Data

The GetAttribute function is used to get the data and put it into a variable. The GetAttribute function is called as follows:

```python
value = obj.GetAttribute(parameter)
```

where `parameter` is a string with the variable name from which data will be retrieved and stored in `value`

For example, consider a thermal rating object called "therm". We can get the thermal ratings data "MyMatrix" as follows:

```python
data = therm.GetAttribute('MyMatrix')
```

## Setting Data

The SetAttribute function is used to put data into an object variable. The SetAttribute function is called as follows:

```python
obj.SetAttribute(parameter, data)
```

where `parameter` is a string with the variable name into which `data` will be stored

For example, consider a thermal rating object called "therm". We can set the "MyMatrix" variable as a 2 x2 matrix as follows:

```python
data = 110, 150], [120, 140
therm.SetAttribute('MyMatrix', data)
```

## Example

This example script creates a vector and matrix object, enters in dummy data and manipulates the matrix data.

[\[ Download example here \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/vectors_matrices.py)

```python
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
```
