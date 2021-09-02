## See the html directory in this repo

import re


def get_name_and_number(input):
    # p = re.compile('\w* has \d* ')
    # p = re.compile(r'\w*has\d*\w*')
    # p = re.compile(r'(\w)*')
    # p = re.compile(r'((\w)*(\s)*)*')
    # p = re.compile(r'((\w)*(\s)*)*[has]')
    # m = p.match(input)
    # if m:
    #    print('Match found: ', m.group())
    # else:
    #    print('No match')

    m = re.match(r"(?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
    # print(m.group('x1'))
    # print(m.group('x2'))
    # print(m.group('x3'))
    r1 = m.group("x1") + " " + m.group("x2")
    r2 = m.group("x4")
    # print(r1)
    # print(r2)
    mytuple = (r1, r2)
    # print(mytuple)
    return mytuple


org01 = "Shewanella colwelliana has 3467 proteins with network connections."
print(get_name_and_number(org01))
