import datetime

# This is a Python set which is nice because we can not
# get any duplication of data...
top = {"ui","psa","ip","t"}
top.add("nly")

def get_day():
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d")
    return y

def build_file_names(top):
    for val in top:
        day = get_day()
        x = f"{val}-fun-{day}"
        print(x)

build_file_names(top)
#get_day()
