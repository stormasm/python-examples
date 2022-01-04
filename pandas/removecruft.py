# from concat import get_symbols_from_filenames, concat
# from dictaryfileread import daryfilereader, get_symbol_from_filename
# from dictdf import process_intermediate_dict
# from init import funmap

import argparse
import os
import pandas as pd


def remove_cruft(df):
    #    for ind in df.index:
    #        print(df["grossprofit"][ind], df["profitmargin"][ind])
    for col in df.columns:
        print(col)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("groupname")
    args = parser.parse_args()
    groupname = args.groupname
    pathtop = os.environ["BMTOP"]
    filename = pathtop + "/bluemesa/tmp/fun/out/" + groupname + ".csv"

    df = pd.read_csv(filename)
    remove_cruft(df)

#    df = pd.DataFrame(d)
#    pd.set_option("display.max_rows", None)
#    print(df)
#    df.to_csv(pathout)
#    print("\nWrote file to ->", pathout)
