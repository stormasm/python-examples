## See the html directory in this repo

import re


def get_name_and_number(input):
    #p = re.compile('\w* has \d* ')
    #p = re.compile(r'\w*has\d*\w*')
    #p = re.compile(r'(\w)*')
    #p = re.compile(r'((\w)*(\s)*)*')
    #p = re.compile(r'((\w)*(\s)*)*[has]')
    #m = p.match(input)
    #if m:
    #    print('Match found: ', m.group())
    #else:
    #    print('No match')

    m = re.match(r"(?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
    print(m.group('x1'))
    print(m.group('x2'))
    print(m.group('x3'))
    print(m.group('x4'))


org01 = "Shewanella colwelliana has 3467 proteins with network connections."
get_name_and_number(org01)
