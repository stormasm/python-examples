import re

def get_date_from_filename(input):
    p = re.compile('(-)[0-9]*(_)')
    q = p.search(input)
    x = q.group()
    x = x[1:9]
    return(x)

a = ["sq-20191231_htm.xml","cube-20200331_htm.xml"]
for x in a:
    value = get_date_from_filename(x)
    print(value)

# references
# https://docs.python.org/3/howto/regex.html
# https://www.pythoncentral.io/how-to-get-a-substring-from-a-string-in-python-slicing-strings/
