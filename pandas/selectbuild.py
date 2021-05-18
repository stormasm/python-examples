from dictaryfileread import daryfilereader, get_symbol_from_filename
from dictdf import process_intermediate_dict
import os
import pandas as pd


def get_df_from_file(filename):
    df = pd.read_csv(filename, sep=",")
    return df


def concat(symbol, symbol_fileary):
    dfary = []
    fileary = symbol_fileary[symbol]
    for file in fileary:
        df = get_df_from_file(file)
        dfary.append(df)
    result = pd.concat(dfary, ignore_index=True)
    return result


def get_symbols_from_filenames(filenames):
    symbols = set()
    for file in filenames:
        symbol = get_symbol_from_filename(file)
        symbols.add(symbol)
    # Turn the set into a list
    return list(symbols)


def select(row, funmap):
    d = {}
    for param in ["mcap", "cashflow"]:
        if row[1] == funmap[param]:
            d[param] = row[2]
    return d


def create_intermediate_dict(symbols, dictfileary, funmap):
    d = {}
    for symbol in symbols:
        list = []
        df = concat(symbol, dictfileary)
        pd.set_option("display.max_rows", None)
        for index, row in df.iterrows():
            dict = select(row, funmap)
            if any(dict.values()):
                list.append(dict)
        d[symbol] = list
    return d


if __name__ == "__main__":
    pathtop = os.environ["BMTOP"]
    #   path1 = pathtop + '/python-examples/data/csv'
    path1 = pathtop + "/bluemesa/tmp/fun/in/test"
    funmap = {
        "cashflow": "Levered Free Cash Flow (ttm)",
        "operatingcashflow": "Operating Cash Flow (ttm)",
        "mcap": "Market Cap",
    }
    files = os.listdir(path1)
    symbols = get_symbols_from_filenames(files)
    dictfileary = daryfilereader(path1, files)
    idict = create_intermediate_dict(symbols, dictfileary, funmap)
    # print(idict)
    d = process_intermediate_dict(idict)
    df = pd.DataFrame(d)
    pd.set_option("display.max_rows", None)
    print(df)
