from os import listdir
from os.path import isfile, join

def getfiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return(onlyfiles)

path1 = '/j/tmp32/bluemesa/tmp'
myfiles = getfiles(path1)
print(myfiles)
