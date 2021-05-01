from dictaryfileread import daryfilereader
import os
import pandas as pd

def get_series_from_file(filename):
    df = pd.read_csv(filename, sep=',')
    return(df)

if __name__ == "__main__":
    pathtop = os.environ['BMTOP']
    path1 = pathtop + '/python-examples/data/csv'
    files = os.listdir(path1)
    d = daryfilereader(path1,files)
    print(d)
    print("\n\n")
    print(d['zm'])
