import argparse
import os
import pandas as pd
import re


def deal_with_million_billion_trillion(val):
    pattern = r"B"
    result = re.sub(pattern, "", val)
    return result


def deal_with_percentage_sign(val):
    pattern = r"%"
    result = re.sub(pattern, "", val)
    return result


def process_type(type, val):
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
    # magic bullet to remove Unnamed: 0 as the first column name
    # https://stackoverflow.com/questions/26098710/rename-unnamed-column-pandas-dataframe/54617685
    df = pd.read_csv(filename, index_col=0)
    df = remove_cruft(df)
    print(df)
