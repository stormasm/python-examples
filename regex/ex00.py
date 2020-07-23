
## Reference
## https://stackoverflow.com/questions/17710921/python-removing-last-character-from-string-using-regex
##

import re
a = ["SDFSD_SFSDF234234","SDFSDF_SDFSDF_234324","TSFSD_SDF_213123"]
c = [re.sub('_?\d+','',x) for x in a]
print(c)
