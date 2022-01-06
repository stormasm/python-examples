from concat import get_symbols_from_filenames, concat
from dictaryfileread import daryfilereader, get_symbol_from_filename
from dictdf import process_intermediate_dict
from init import funmap
from removecruft import remove_cruft

import argparse
import os
import pandas as pd


def select(row, funmap):
    d = {}
    for param in ["mcap", "revenue", "grossprofit", "operatingmargin", "profitmargin"]:
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

    parser = argparse.ArgumentParser()
    parser.add_argument("groupname")
    args = parser.parse_args()
    groupname = args.groupname

    pathtop = os.environ["BMTOP"]

    # For testing only
    # path1 = pathtop + "/python-examples/data/csv"

    path1 = pathtop + "/bluemesa/tmp/fun/in/" + groupname
    pathout = pathtop + "/bluemesa/tmp/fun/out/" + groupname + ".csv"
    files = os.listdir(path1)
    symbols = get_symbols_from_filenames(files)
    dictfileary = daryfilereader(path1, files)
    idict = create_intermediate_dict(symbols, dictfileary, funmap)
    # print(idict)
    d = process_intermediate_dict(idict)
    df = pd.DataFrame(d)
    pd.set_option("display.max_rows", None)
    df = remove_cruft(df)
    print(df)
    df.to_csv(pathout)
    print("\nWrote file to ->", pathout)
