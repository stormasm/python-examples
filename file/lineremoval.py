import os
from os import listdir
from os.path import isfile, join

def getfilename_withtmp(filename):
    oldname = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    newname = oldname + "-tmp" + extension
    return(newname)

def getfiles_old(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return(onlyfiles)

def getfiles(mypath):
    files = set()
    for file in os.listdir(mypath):
        if file.endswith(".csv"):
            files.add(os.path.join(mypath, file))
    return(files)

def removeline(filename):
    newname = getfilename_withtmp(filename)
    print(newname)

def removeline1(filename):
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
        removeline1(file)
