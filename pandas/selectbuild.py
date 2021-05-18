from dictaryfileread import daryfilereader, get_symbol_from_filename
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
    for param in ["mcap", "cashflow"]:
        if row[1] == funmap[param]:
            print(param, row[2])


def process(symbols, dictfileary, funmap):
    for symbol in symbols:
        print(symbol)
        df = concat(symbol, dictfileary)
        pd.set_option("display.max_rows", None)
        for index, row in df.iterrows():
            select(row, funmap)


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
    process(symbols, dictfileary, funmap)
