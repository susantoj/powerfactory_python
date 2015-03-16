## Accessing project folders

Each folder in the PowerFactory project tree (e.g. Library, Network Model, Diagrams, etc) are objects that can be accessed by Python code.

PowerFactory contains a method GetProjectFolder that returns common project folders. The general usage is as follows:

```python
import powerfactory as pf
app = pf.GetApplication()
prj_folder = app.GetProjectFolder(folder_string)
```

where `folder_string` is a string code for a particular project folder.

PowerFactory supports the following `folder_strings`:

| folder_string | Folder description     |
| ------------- | ---------------------- |
| equip         | Equipment type library |
| netmod        | Network model          |
| oplib         | Operational library    |
| scen          | Operational scenario   |
| script        | Script library (local) |
| study         | Study case             |
| templ         | Template               |
| netdat        | Network data           |
| dia           | Diagram                |
| scheme        | Variation              |
| cbrat         | CB rating              |
| therm         | Thermal rating         |
| ra            | Running arrangement    |
| mvar          | MVAr limit curve       |
| outage        | Outages (operational library) | 
| fault         | Faults (operational library)  |

You will notice that not all of the folders in the project tree are not accessible by the GetProjectFolder function. Other folders can be accessed by using the GetParent and GetContents functions to traverse up and down the hierarchy respectively.

For example, to get to the "User Defined Models" folder, one can traverse up from the equipment library (to get the main library folder) and then down to get the User Defined Models folder.

```python
equip = app.GetProjectFolder('equip')
lib_fold = equip.GetParent()
udm_fold = lib_fold.GetContents('User Defined Models.IntPrjFolder')[0][0] 
```

## Example

This example script returns objects for most of the commonly used folders in the PowerFactory project tree.

[\[Download example here\]](https://github.com/susantoj/powerfactory_python/blob/master/examples/project_folders.py)

```python
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
```
