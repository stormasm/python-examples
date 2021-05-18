# So this takes in
# files = os.listdir(path1)
# and returns a dict with the
# key being the symbol and the
# value being the array of filenames
# for that particular symbol
#
# the nice thing about this implementation
# is that different symbols can have a different
# number of csv files as input

import os
from pathlib import PurePath
import re


def get_symbol_from_filename(filename):
    pp = PurePath(filename)
    # get the filename in the path
    p1 = pp.parts[-1]
    # get everything before the dot
    p2 = re.split("-", p1)[0]
    return p2


def add_file_to_dict(dict, symbol, filename):
    # check to see if this symbol is in the dict
    if symbol in dict:
        ary = dict[symbol]
        ary.append(filename)
        return dict
    ary = []
    ary.append(filename)
    dict[symbol] = ary
    return dict


def daryfilereader(filepath, files):
    d = {}
    for file in files:
        filename = os.path.join(filepath, file)
        symbol = get_symbol_from_filename(filename)
        d = add_file_to_dict(d, symbol, filename)
    return d


if __name__ == "__main__":
    pathtop = os.environ["BMTOP"]
    path1 = pathtop + "/python-examples/data/csv"
    files = os.listdir(path1)
    d = daryfilereader(path1, files)
    print(d)
    print("\n\n")
    print(d["zm"])
