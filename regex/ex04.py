## See the html directory in this repo

import re

def get_name_and_number(input):
    m = re.match(r"(?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
    r1 = m.group("x1") + " " + m.group("x2")
    r2 = m.group("x4")
    mytuple = (r1, r2)
    return mytuple

org01 = "Shewanella colwelliana has 3467 proteins with network connections."
print(get_name_and_number(org01))
