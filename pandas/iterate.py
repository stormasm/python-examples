import argparse
import os
import pandas as pd


def iterate(df):
    for ind in df.index:
        for col in df.columns:
            print(df[col][ind])


def iterate_1(df):
    for col in df.columns:
        print(col)


def iterate_2(df):
    for ind in df.index:
        print(df.loc[ind])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("groupname")
    args = parser.parse_args()
    groupname = args.groupname
    pathtop = os.environ["BMTOP"]
    filename = pathtop + "/bluemesa/tmp/fun/out/" + groupname + ".csv"
    df = pd.read_csv(filename)
    iterate(df)
