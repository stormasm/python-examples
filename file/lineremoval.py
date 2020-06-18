# This removes the first line of a file
#
# Be careful running this script because
# if you run it twice it will continue to
# remove the first line

import os
from os import listdir
from os.path import join

def getfilename_withtmp(filename):
    oldname = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    newname = oldname + "-tmp" + extension
    return(newname)

def getfiles(mypath):
    files = set()
    for file in os.listdir(mypath):
        if file.endswith(".csv"):
            files.add(os.path.join(mypath, file))
    return(files)

def removeline(filename):
    filenametmp = getfilename_withtmp(filename)
    with open(filename,'r') as f:
        with open(filenametmp,'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)
    os.remove(filename)
    os.rename(filenametmp,filename)

if __name__ == "__main__":
    path = '/tmp/t1/p1'
    files = getfiles(path)
    for file in files:
        removeline(file)
        print("Removed the first line of " + file)
