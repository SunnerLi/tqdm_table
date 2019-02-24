from tqdm_table import tqdm_table
import random
import time

bar = tqdm_table(range(4))
bar.set_table_setting(max_length=150)
for i in bar:
    """
        ...
        Do something you want
        ...
    """
    mapping = {
        'variable1': round(random.random(), 5),
        'variable2': round(random.random(), 5),
        'variable3': round(random.random(), 5),
        'variable4': round(random.random(), 5),
        'variable5': round(random.random(), 5),
        'variable6': round(random.random(), 5),
    }
    bar.set_table_info(mapping)
    time.sleep(1.5)