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
    sseries = df['Symbol']
    svalues = sseries.values
    # convert strings in array to lowercase
    svlc = map(str.lower, svalues)
    svl = tuple(svlc)

    nseries = df['Company Name']
    nvalues = nseries.values
    nvl = tuple(nvalues)

    return(svl,nvl)

#your_path = '/j/tmp32/python-examples/data/sp500'
your_path = '/j/tmp32/equity-data/sp500/groups/200507'
files = os.listdir(your_path)
d = {}
for file in files:
    filename = os.path.join(your_path, file)
    tsn = get_dict(filename)
    print(tsn[0])
    print(tsn[1])
#myj = json.dumps(arr)
#print(myj)
