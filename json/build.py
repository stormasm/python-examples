import os
import pandas as pd
from pathlib import PurePath
import re

def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("\.",p1)[0]
    # get everything after holdings-
    p3 = re.split("holdings-",p2)[1]
    return(p3)

def process(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Symbol']
    values = series.values
    symbol = get_symbol_from_filename(filename)
    print(symbol)

your_path = '/j/tmp32/python-examples/data/sp500'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path, file)
    process(filename)
