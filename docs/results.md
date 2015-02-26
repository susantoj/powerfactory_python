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
