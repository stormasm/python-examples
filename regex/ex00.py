
## Reference
## https://stackoverflow.com/questions/17710921/python-removing-last-character-from-string-using-regex
##

import re
a = ["SDFSD_SFSDF234234","SDFSDF_SDFSDF_234324","TSFSD_SDF_213123"]
c = [re.sub('_?\d+','',x) for x in a]
print(c)

# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub('\s', '9', txt)
print(x)

# Replace every B character with nothing:
a = ["123.45B","23B"]
c = [re.sub('B', '', x) for x in a]
print(c)

#a = ["123.45B","34.56M"]
#c = [re.sub('\d+(?:\.\d+)?))','',x) for x in a]
#print(c)

#  (\d+(?:\.\d+)?)

#a = 1.1
#c = re.sub('(\d+(?:\.\d+)?)','',a)
#print(c)
