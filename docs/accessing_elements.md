## Accessing network elements

The most convenient way to access elements in the network is to use the `GetCalcRelevantObjects` function, which allows you to filter network elements by name and type. This method is included in the PowerFactory `application` object and returns a list. 
General usage is as follows:

```python
import powerfactory as pf
app = pf.GetApplication()
returned_list = app.GetCalcRelevantObjects(filter)
```

where `returned_list` is a list of objects that is returned by the function. If nothing is found, then an empty list [] is returned.
`filter` is a string parameter that describes which network objects you want to return (more on this below)

### Filter Examples
Filters are strings that describe which objects you want from the query. The asterisk (*) is a wildcard character that denotes the matching of zero or more characters. 

Here are some examples of filters:

a) Get all network objects (including types)

```python
all_objs = app.GetCalcRelevantObjects('*')
```

b) Get all line elements

```python
lines = app.GetCalcRelevantObjects('*.ElmLne')
```

c) Get lines with a name starting with '86'

```python
lines = app.GetCalcRelevantObjects('86*.ElmLne')
```

d) Get the specific line with name 'line_3a'

```python
line_3a = app.GetCalcRelevantObjects('line_3a.ElmLne')
```

e) Get all line types (that are being used, i.e. does not include unused types in the library)

```python
line_types = app.GetCalcRelevantObjects('*.TypLne') 
```

### Example
This example script gets lists of buses, generators and lines in the network and then creates dictionaries for each element type (e.g. dictionary of buses, generators and lines).

[\[Download example here\]](https://github.com/susantoj/powerfactory_python/blob/master/examples/element_dictionaries.py)

```python
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
```
