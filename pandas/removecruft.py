import argparse
import os
import pandas as pd


def deal_with_million_billion_trillion(val):
    result = 2.0
    return result


def deal_with_percentage_sign(val):
    result = 1.0
    return result


def process_type(type, val):
    print(type)
    print(val)
    if type == "operatingmargin":
        result = deal_with_percentage_sign(val)
        return result
    elif type == "profitmargin":
        result = deal_with_percentage_sign(val)
        return result
    else:
        result = deal_with_million_billion_trillion(val)
        return result
    other = 123456.7
    return other


def process_cruft(type, val):
    result = process_type(type, val)
    return result


def remove_cruft(df):
    for ind in df.index:
        for col in df.columns:
            result = process_cruft(col, df[col][ind])
            df[col][ind] = result
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
