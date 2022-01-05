import argparse
import os
import pandas as pd


def remove_cruft(df):
    for ind in df.index:
        for col in df.columns:
            print(df[col][ind])
            df[col][ind] = 1.0
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("groupname")
    args = parser.parse_args()
    groupname = args.groupname
    pathtop = os.environ["BMTOP"]
    filename = pathtop + "/bluemesa/tmp/fun/out/" + groupname + ".csv"
    df = pd.read_csv(filename)
    df = remove_cruft(df)
    print(df)
