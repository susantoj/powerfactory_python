## Characteristics

In PowerFactory, characteristics are a way of assigning values to object parameters based on a "trigger" and "scale". The way characteristics are set up in PowerFactory is generic and quite abstract, so is best illustrated by examples.

**Example 1**: a load profile with a series of active power demands (in MW) in hourly intervals is assigned to a load. In this case, the trigger is the study time and the scale is time (hours). When the study time is changed, the value of the load changes correspondingly according to the load profile.

**Example 2**: a capacitor bank is switched on and off depending on an operating mode: Low Load, Medium Load and High Load. In this case, a characteristic is assigned to the "out of service" flag of the capacitor bank. The scale is the range of applicable operating modes (low, medium and high) and the trigger is the current operating mode. When the operating mode is changed, the capacitor bank is switched on or off depending on the characteristic.

**Example 3**: a wind turbine's power coefficient (Cp) is calculated from a lookup table based on two inputs: tip-speed ratio and blade pitch. In this case, the characteristic is assigned to the power output of the wind turbine. The characteristic is a matrix with two triggers (tip-speed ratio and blade pitch) and two scales (range of tip-speed ratios and range of blade pitches). Changing either of the triggers will change the wind turbine output accordingly.

## Creating Characteristics

Characteristics are simply PowerFactory objects and can be created with the **CreateObject()** function. However, the data still needs to be entered into the characteristic. An efficient way to create characteristics is to automatically import data from a CSV file and then enter it automatically into characteristics.

[\[ Example for creating time characteristics from a CSV file \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/create_time_characteristics.py)

[\[ CSV file for example \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/loads_file.csv)

## Assigning Characteristics

Once characteristics have been created, they still need to be assigned to an object parameter, e.g. load active power (Plini) or out of service flag (outserv). This is done through characteristic reference objects, which link a characteristic in the library to parameters in the network model. This allows a single characteristic to be reused in multiple object parameters.

[\[ Example for assigning characteristics \]](https://github.com/susantoj/powerfactory_python/blob/master/examples/assign_characteristics.py)
