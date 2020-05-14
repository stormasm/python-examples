import json
import os
import pandas as pd
import re

def get_tuples(filename):
    df = pd.read_csv(filename, sep=',')
    sseries = df['Symbol']
    svalues = sseries.values
    # convert strings in array to lowercase
    svlc = map(str.lower, svalues)
    svl = tuple(svlc)

    nseries = df['Company Name']
    nvalues = nseries.values
    nvl = tuple(nvalues)

    return(svl,nvl)

your_path = '/j/tmp32/equity-data/sp500/groups/200507'
files = os.listdir(your_path)
d = {}
for file in files:
    filename = os.path.join(your_path, file)
    tsn = get_tuples(filename)
    symbols = tsn[0]
    names = tsn[1]
    for s, n in zip(symbols, names):
        d[s] = n
myj = json.dumps(d)
print(myj)
