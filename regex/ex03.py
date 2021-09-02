## See the html directory in this repo

import re


def get_name_and_number(input):
    p = re.compile('\w* has \d* ')
    m = p.match(input)
    if m:
        print('Match found: ', m.group())
    else:
        print('No match')


org01 = "Shewanella colwelliana has 3467 proteins with network connections."
get_name_and_number(org01)
