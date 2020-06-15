import datetime

# This is a Python set which is nice because we can not
# get any duplication of data...
top = {"ui","psa","ip","t"}
top.add("nly")

def get_day():
    now = datetime.datetime.now()
    print(now)

def build_file_names(top):
    for val in top:
        print(val)

#build_file_names(top)
get_day()
