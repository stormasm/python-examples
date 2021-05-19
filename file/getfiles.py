import glob
import os
from os import listdir
from os.path import isfile, join


def getsymbolfiles(mypath, symbol):
    hits = []
    pattern = mypath + "/" + symbol + "-*.csv"
    for name in glob.glob(pattern):
        hits.append(name)
    return hits


def getfiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


if __name__ == "__main__":
    path = os.environ["BMTOP"]
    path = path + "/bluemesa/tmp/fun/in/test"
    myfiles = getfiles(path)
    mysymbolfiles = getsymbolfiles(path, "ibm")
    print(myfiles)
    print("\n")
    print(mysymbolfiles)
