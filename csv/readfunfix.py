#
#  This file fixes the fact that the first rows attribute and value
#  are capitalized so it changes it to lower case...
#

import csv

with open("ui-fun.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    for idx, row in enumerate(spamreader):
        if (idx == 0):
            row = ['', 'attribute', 'value']
            print(", ".join(row))
        else:
            print(", ".join(row))
