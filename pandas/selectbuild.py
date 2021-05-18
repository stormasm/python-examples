from dictaryfileread import daryfilereader, get_symbol_from_filename
import os
import pandas as pd

def get_df_from_file(filename):
    df = pd.read_csv(filename, sep=',')
    return(df)

def concat(symbol,symbol_fileary):
    dfary = []
    fileary = symbol_fileary[symbol]
    for file in fileary:
        df = get_df_from_file(file)
        dfary.append(df)
    result = pd.concat(dfary,ignore_index=True)
    return(result)

def get_symbols_from_filenames(filenames):
    symbols = set()
    for file in filenames:
        symbol = get_symbol_from_filename(file)
        symbols.add(symbol)
    # Turn the set into a list
    return(list(symbols))

if __name__ == "__main__":
    pathtop = os.environ['BMTOP']
#   path1 = pathtop + '/python-examples/data/csv'
    path1 = pathtop + '/bluemesa/tmp/fun/in/test'

    files = os.listdir(path1)
    symbols = get_symbols_from_filenames(files)
    d = daryfilereader(path1,files)
    for symbol in symbols:
        print('\n')
        print(symbol)
        print('\n')
        df = concat(symbol,d)
        pd.set_option('display.max_rows', None)
        for index,row in df.iterrows():
            print(type(row[1]),row[1])
