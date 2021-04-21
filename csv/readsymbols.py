import csv
with open('symbols.csv', newline='') as csvfile:
    symbolreader = csv.reader(csvfile, delimiter=',')
    symboldict = {};
    for row in symbolreader:
        symboldict[row[0]] = row[1]
    print(symboldict.items())
    print(symboldict['adbe'])
