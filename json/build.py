
import os
import pandas as pd


def get_series_array(series):
    print(series.values)

def process(filename):
    df = pd.read_csv(filename, sep=',')
    symbols_series = df['Symbol']
    get_series_array(symbols_series)

your_path = '/j/tmp32/python-examples/data/sp500'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path,file)
    print(filename)
    process(filename)
