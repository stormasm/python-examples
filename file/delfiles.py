# Shows how to delete files

import glob
import os
from os import listdir
from os.path import isfile, join


def deletefile(filename):
    if os.path.exists(filename):
        os.remove(filename)


def getsymbolfiles(mypath, symbol):
    hits = []
    pattern = mypath + "/" + symbol + "-*.csv"
    for name in glob.glob(pattern):
        hits.append(name)
    return hits


def deletesymbolfiles(filenames):
    for filename in filenames:
        deletefile(filename)


if __name__ == "__main__":
    path = os.environ["BMTOP"]
    # path = path + "/bluemesa/tmp/fun/in/test"
    path = "/tmp/fun"
    symbolfiles = getsymbolfiles(path, "ui")
    print(symbolfiles)
    for filename in symbolfiles:
        print(filename)
        deletefile(filename)
