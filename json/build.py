
import os
import pandas as pd

def process(filename):
    df = pd.read_csv(filename, sep=',')
    print(df)

your_path = '/j/tmp32/python-examples/data/sp500'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path,file)
    print(filename)
    process(filename)
