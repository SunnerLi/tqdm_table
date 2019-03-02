# tqdm_table
### A simple toolkit to create table with tqdm

[![Packagist](https://img.shields.io/badge/Python-3.5.2-blue.svg)]()
[![Packagist](https://img.shields.io/badge/OS-Ubuntu_16.04-orange.svg)]()
![](https://github.com/SunnerLi/tqdm_table/blob/master/img/example_result.gif)

Abstraction
---
This toolkit can help you to create a simple table with `tqdm` package.    

Install
---
```
git clone https://github.com/SunnerLi/tqdm_table.git && mv tqdm_table/tqdm_table tqdm_table_actual && rm -rf tqdm_table && mv tqdm_table_actual tqdm_table
```

Usage
---
```python
from tqdm_table import tqdm_table

bar = tqdm_table(range(4))
for i in bar:
    # Do something you want
    mapping = {
        'variable1': 1,
        'variable2': 2
    }
    bar.set_table_info(mapping)
```

There are only 2 function:
```python
# Change the maximun width of table
tqdm_table.set_table_setting(max_length=150)

# Print the table for the given dict object
tqdm_table.set_table_info(mapping)
```