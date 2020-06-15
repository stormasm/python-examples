import datetime
from yahoo_fin.stock_info import get_stats

# This is a Python set which is nice because we can not
# get any duplication of data...
symbols = {"ui","psa","ip","t"}
symbols.add("nly")

def get_day():
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d")
    return y

def build_file_name(symbol):
    day = get_day()
    filename = f"{symbol}-fun-{day}.csv"
    return(filename)

def process():
    for symbol in symbols:
        print(symbol)
        filename = build_file_name(symbol)
        data = get_stats(symbol)
        data.to_csv(filename)

process()
