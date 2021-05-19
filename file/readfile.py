import os

# This should return a set of symbols
def get_symbols(filename):
    myset = set()
    fp = open(filename, "r")
    for cnt, line in enumerate(fp):
        symbol = line.strip()
        myset.add(symbol)
    return myset


if __name__ == "__main__":
    path = os.environ["BMTOP"]
    path = path + "/equity-data/symbols/top.txt"
    mysymbols = get_symbols(path)
    print(mysymbols)
