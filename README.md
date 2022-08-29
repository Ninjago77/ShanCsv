# ShanCsv <br/>[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/) [![Pip latest](https://img.shields.io/badge/pip-latest-blue)](https://pip.pypa.io/en/stable/) [![license](https://img.shields.io/badge/license-MIT-green)](https://github.com/Ninjago77/ShanCsv/blob/main/LICENSE)
A [Python Package](https://pypi.org/) for [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) File Parsing and Rendering. Easy to use and follows the formats of other commonly used libraries - The [load(s)](#shancsvloadfile)/[dump(s)](#shancsvdumpdata-file) functions of [pickle](https://docs.python.org/3/library/pickle.html)/[json](https://docs.python.org/3/library/json.html). Automatically converts data values from/to a 2-dimensional list as *float, int, bool, none, str* unlike the [in-built csv library.](https://docs.python.org/3/library/csv.html)
Completly customizable by giving the specified \*\**kwargs* to the [`Csv Class`](#shancsvcsvinputobj-inputtypestr-moreargs) directly or through the [other functions](#basic-usage) indirectly. Simple, readable, easy to understand [Docs.](https://github.com/Ninjago77/ShanCsv#readme) So what are you waiting for? Install [ShanCsv](#how-to-install) and try it now!
## How to install
Install the [`ShanCsv`](https://pypi.org/project/ShanCsv/) module using [`pip`](https://pip.pypa.io/en/stable/)
```bash
pip install ShanCsv
```
Then import the [`ShanCsv`](https://pypi.org/project/ShanCsv/) module into your program
```python
import shancsv
```
## Basic Usage
### <sup>*shancsv*</sup>.dump(data, file)
 - Writes the data (2-dimensional list) in CSV format to the file
 - Other Arguments are transferred to [`dumps`](#shancsvdumpsdata) and [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
 with open("test.csv","w") as file:
    shancsv.dump(data, file) # data is a 2-dimensional list
 ```
### <sup>*shancsv*</sup>.dumps(data)
 - Returns the data (2-dimensional list) in CSV format as *str*
 - Other Arguments are transferred to [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
text = shancsv.dumps(data) # data is a 2-dimensional list
 ```
### <sup>*shancsv*</sup>.load(file)
 - Reads the file in CSV format and converts it to data (2-dimensional list)
 - Other Arguments are transferred to [`loads`](#shancsvloadstext-gettype) and [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
 with open("test.csv","r") as file:
    data = shancsv.load(file) # data is a 2-dimensional list
 ```
### <sup>*shancsv*</sup>.loads(text, *getType*)
 - Returns the CSV format converted to data (2-dimensional list) as *list*\*
 - The *getType* argument can have any of these values *(list, tuple, str)*, by default it is *list*
 - Other Arguments are transferred to [`Csv`](#shancsvcsvinputobj-inputtypestr-moreargs)
 - Example:
```python
data = shancsv.loads(text) # data is a 2-dimensional list
 ```
### <sup>*shancsv*</sup>.Csv(inputObj, *inputTypeStr*, \**MoreArgs*)
 - A Csv Object that takes an *inputObj* and handles almost everything needed for parsing and rendering CSV data
 - The *inputTypeStr* argument is a *boolean* value that specifies if the *inputObj* is a *str*, by default it is *True*
 - \**MoreArgs* = *delimiter, lineterminator, boolValue, noneValue, floatValue, intValue, customTrueValue, customFalseValue, customNoneValue*
  - \**MoreArgs* Docs coming soon!
 - Example:
```python
c = shancsv.Csv(text)
data = c.getList() # data is a 2-dimensional list
text = str(c)
 ```
