
import os
import pandas as pd

your_path = '/j/tmp32/python-examples/data/csv'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path,file)
    print(filename)
    df = pd.read_csv(filename, sep=',')
    print(df)
