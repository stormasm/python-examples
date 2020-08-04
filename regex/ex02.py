import re

def get_date_from_filename(input):
    c = re.search('(-)[0-9]*(_)', input)
    return(c)

a = ["sq-20200331_htm.xml","cube-20200331_htm.xml"]
for x in a:
    value = get_date_from_filename(x)
    print(value)
