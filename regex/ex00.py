## Reference
## https://stackoverflow.com/questions/17710921/python-removing-last-character-from-string-using-regex
##

import re

a = ["SDFSD_SFSDF234234", "SDFSDF_SDFSDF_234324", "TSFSD_SDF_213123"]
c = [re.sub("_?\d+", "", x) for x in a]
print(c)

# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Replace every M,B,% character with nothing:
a = ["123.45B", "23B", "234M", "434.12B", "34%", "56.1%"]
c = [re.sub("[M,B,%]", "", x) for x in a]
print(c)
