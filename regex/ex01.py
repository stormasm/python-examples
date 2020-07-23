import re

def remove_unwanted_chars(input):
    c = re.sub('[M,B,%,$]', '', input)
    return(c)

# Replace every M,B,% character with nothing:
a = ["$123.45B","23B","234M","$434.12B","34%","56.1%"]
for x in a:
    value = remove_unwanted_chars(x)
    print(value)
