## Running calculations

Calculations in PowerFactory (such as load flows, short circuits, time-domain simulations, etc) are controlled by Command objects (*.Com*), which reside in the study case folders. The simplest way to create a command object or access an existing one in the active study case is to use the `GetFromStudyCase` function. The `Execute` function is then used to run the calculation.

General usage is as follows (the snippet below gets a short circuit object and runs a fault calculation):

```python
import powerfactory as pf

app = pf.GetApplication()

shc = app.GetFromStudyCase('ComShc')
shc.Execute()
```

Note that the GetFromStudyCase function looks for an existing command object in the active study case. If a command object is not found, then it will create a new one. 

Commonly used command objects are as follows:
- ComLdf (Load flow)
- ComShc (Short Circuit)
- ComStatsim (Quasi-dynamic simulation)
- ComSimoutage (Contingency analysis)
- ComNmink (Contingency definition)
- ComInc (Initial conditions for time domain simulation)
- ComSim (Run time domain simulation)

The command objects also include the setup parameters for the calculation. For example, the ComShc object contains parameters such as the calculation method (IEC, ANSI, etc), the type of fault (3-Phase, 2-Phase, Earth Fault, etc) and the fault impedance (R and X). These parameters can also be modified in script. For example, to set the calculation method to IEC, the "iopt_mde" parameter needs to be modified as follows"
```python
shc.iopt_mde = 1
```

## Example

This example script gets a short circuit calculation object, sets it up and runs a short circuit calculation.

[\[ Download example here \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/run_calc.py)

```python
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
```
