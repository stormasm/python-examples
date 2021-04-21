import csv
import os

path = os.environ['BMTOP']
symbol_filename = path + '/bluemesa/data/symbols.csv'

def get_symbol_name(symbol):
    with open(symbol_filename, newline='') as csvfile:
        symbolreader = csv.reader(csvfile, delimiter=',')
        symboldict = {};
        for row in symbolreader:
            symboldict[row[0]] = row[1]
        return(symboldict[symbol])

if __name__ == "__main__":
    print(get_symbol_name('intu'))
