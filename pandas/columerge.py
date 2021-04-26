import csv
import os
import pandas as pd
from pathlib import PurePath
import re

def modify_array_values(input):
    arr = []
    for value in input:
        mytype = type(value)
        bool = isinstance(value,(float,tuple))
        if not bool:
            arr.append(value)
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

def get_array(filename):
    df = pd.read_csv(filename, sep=',')
    series = df['Value']
    values = series.values
    values = modify_array_values(values)
    symbol = get_symbol_from_filename(filename)
    values.insert(0,symbol)
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
    print(dict_schema)


#    files = os.listdir(path1)

#    with open('columerge.csv', 'w', newline='') as csvfile:
#        csvwriter = csv.writer(csvfile, delimiter=',')
#        csvwriter.writerow(fieldnames)
#        for file in files:
#            filename = os.path.join(path1, file)
#            d = get_array(filename)
#            csvwriter.writerow(d)
