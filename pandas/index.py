import csv
import os
import pandas as pd
from pathlib import PurePath
import re

def force_float(elt):

    try:
        return float(elt)
    except:
        return elt

def _convert_to_numeric(s):

    if "M" in s:
        s = s.strip("M")
        v = force_float(s) / 1000
        return(round(v,5))

    if "B" in s:
        s = s.strip("B")
        return force_float(s)

    return force_float(s)

def modify_array_values(input):
    arr = []
    for value in input:
        mytype = type(value)
        bool = isinstance(value,(float,tuple))
        if not bool:
            myvalue = _convert_to_numeric(value)
            arr.append(myvalue)
        else:
            arr.append("N/A")
    return(arr)

def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("-fun",p1)[0]
    return(p2)

def get_series_from_file(filename):
    df = pd.read_csv(filename, sep=',')
    #print(df)
    series = df['Value']
    values = series.values
    #print(values)
    values = modify_array_values(values)
    #print(values)
    return(values)

# This returns a dict with the original name and the new name
def read_schema_to_dict(path):
    d = {}
    with open(path, newline='') as csvfile:
        funreader = csv.reader(csvfile, delimiter=',')
        # do not read the first line of the csv file
        next(funreader)
        for row in funreader:
            d[row[1]] = row[2]
    return(d)

if __name__ == "__main__":
    pathtop = os.environ['BMTOP']
    path1 = pathtop + '/python-examples/data/csv'
    path2 = pathtop + '/python-examples/data/schema-fun.csv'

    dict_schema = read_schema_to_dict(path2)
    ary = []
    for key in dict_schema:
        ary.append(dict_schema[key])
    files = os.listdir(path1)
    d = {}
    for file in files:
        filename = os.path.join(path1, file)
        series = get_series_from_file(filename)
        symbol = get_symbol_from_filename(filename)
        d[symbol] = series
    df = pd.DataFrame(d,index=ary)
    print(df[['ui','ibm','rdfn']])
