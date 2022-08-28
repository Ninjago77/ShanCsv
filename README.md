# ShanCsv
A Python Package for CSV File Parsing and Rendering
## How to install
Install the [`ShanCsv`](https://pypi.org/project/ShanCsv/) module using [`pip`](https://pip.pypa.io/en/stable/)
```bash
pip install ShanCsv
```
Then import the [`ShanCsv`](https://pypi.org/project/ShanCsv/) module into your program
```python
import ShanCsv
```
## Basic Usage
### <sup>*ShanCsv*</sup>.dump(data, file)
 - Writes the data (2-dimensional list) in CSV format to the file
 - Other Arguments are transferred to [`dumps`](#shancsvdumpsdata) and [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
 with open("test.csv","w") as file:
    ShanCsv.dump(data, file) # data is a 2-dimensional list
 ```
### <sup>*ShanCsv*</sup>.dumps(data)
 - Returns the data (2-dimensional list) in CSV format as str
 - Other Arguments are transferred to [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
text = ShanCsv.dumps(data) # data is a 2-dimensional list
 ```
### <sup>*ShanCsv*</sup>.load(file)
 - Reads the file in CSV format and converts it to data (2-dimensional list)
 - Other Arguments are transferred to [`loads`](#shancsvloadstext-gettype) and [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
 with open("test.csv","r") as file:
    data = ShanCsv.load(file) # data is a 2-dimensional list
 ```
### <sup>*ShanCsv*</sup>.loads(text, *getType*)
 - Returns the CSV format converted to data (2-dimensional list) as list\*
 - The *getType* argument can have any of these values (list, tuple, str), by default it is list
 - Other Arguments are transferred to [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
data = ShanCsv.loads(text) # data is a 2-dimensional list
 ```
### <sup>*ShanCsv*</sup>.Csv(inputObj, *inputTypeStr*, \**MoreArgs*)
 - A Csv Object that takes an inputObj and handles almost everything needed for parsing and rendering CSV data
 - The *inputTypeStr* argument is a boolean value that specifies if the inputObj is a str, by default it is True
 - \**MoreArgs* = *itemSplitter, lineSplitter, boolValue, noneValue, floatValue, intValue, customTrueValue, customFalseValue, customNoneValue*
  - \**MoreArgs* Docs coming soon!
 - Example:
```python
c = ShanCsv.Csv(text)
data = c.getList() # data is a 2-dimensional list
text = str(c)
 ```
