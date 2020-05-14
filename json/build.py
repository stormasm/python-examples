import os
import pandas as pd
from pathlib import PurePath

def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    p1 = pp.parts
    print(p1[-1])

def process(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Symbol']
    values = series.values
    get_symbol_from_filename(filename)
    #print(filename, values)

your_path = '/j/tmp32/python-examples/data/sp500'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path, file)
    process(filename)
