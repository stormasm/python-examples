import json
import os
import pandas as pd
from pathlib import PurePath
import re

def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("\.",p1)[0]
    # get everything after holdings-
    p3 = re.split("holdings-",p2)[1]
    return(p3)

def get_dict(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Symbol']
    values = series.values
    d = {}
    symbol = get_symbol_from_filename(filename)
    st = tuple(values)
    d[symbol] = st
    return(d)

your_path = '/j/tmp32/python-examples/data/sp500'
files = os.listdir(your_path)
ja = []
for file in files:
    filename = os.path.join(your_path, file)
    d = get_dict(filename)
    ja.append(d)
t2 = json.dumps(ja)
print(t2)
