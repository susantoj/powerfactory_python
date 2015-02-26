## Getting calculation results

Calculation results (such as load flow or short circuit results) can be extracted by using either the `GetAttribute` or `getattr` functions:

1) The `GetAttribute` function is a method that is included in every PowerFactory object. For example, consider the bus object (*.ElmTerm) called "bus". The GetAttribute function is called as follows:

```python
value = bus.GetAttribute(parameter)
```

where `parameter` is a string with the result variable of interest, e.g. 'm:u' for bus voltage, 'm:phiu' for bus angle, etc.

2) The `getattr` function is a generic Python method that takes an object as an explicit parameter, i.e.

```python
value = getattr(obj, parameter)
```

where `obj` is a PowerFactory data object (such as a bus) and `parameter` is a string with the result variable of interest.

## Example
This example script runs a load flow and gets bus voltages and line loadings.

[\[ Download example here \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/results.py)

```python
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
```
