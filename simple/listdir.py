
import os
import pandas as pd

your_path = '/j/tmp32/equity-data/sp500/groups/200507'
files = os.listdir(your_path)
for file in files:
    filename = os.path.join(your_path,file)
    print(filename)
    df = pd.read_csv(filename, sep=',')
    print(df)
