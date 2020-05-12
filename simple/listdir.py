import os
your_path = '/j/tmp32/equity-data/sp500/groups/200507'
files = os.listdir(your_path)
for file in files:
    print(file)
    if os.path.isfile(file):
        f=open(os.path.join(your_path,file),'r')
        for x in f:
            print(x)
        f.close()
