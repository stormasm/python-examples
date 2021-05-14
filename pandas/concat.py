from dictaryfileread import daryfilereader
import os
import pandas as pd

def get_df_from_file(filename):
    df = pd.read_csv(filename, sep=',')
    return(df)

if __name__ == "__main__":
    pathtop = os.environ['BMTOP']
#   path1 = pathtop + '/python-examples/data/csv'
    path1 = pathtop + '/bluemesa/tmp/fun/in/test'

    files = os.listdir(path1)
    d = daryfilereader(path1,files)
#   print(d)
#   print("\n\n")
#   print(d['zm'])
    dfary = []
    fileary = d['ibm']
    for file in fileary:
        df = get_df_from_file(file)
        dfary.append(df)
    result = pd.concat(dfary)
    pd.set_option('display.max_rows', None)
    print(result)
