import csv
import re

def get_name_and_number(input):
    m = re.match(r"(?P<x0>Organism) (?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
    if m == None:
        return None
    r1 = m.group("x1") + " " + m.group("x2")
    r2 = m.group("x4")
    mytuple = (r1, r2)
    return mytuple



#def get_name_and_number(input):
#    print(type(input))
#    print(input)
#    m = re.match(r"(?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input)
#    print(m)
#    if m == None:
#        return None
#    r1 = m.group("x1") + " " + m.group("x2")
#    r2 = m.group("x4")
#    mytuple = (r1, r2)
#    print(mytuple)
#    return mytuple

def process_row(row):
    value = row[1]
    #print(value)
    org01 = "Shewanella colwelliana has 3467 proteins with network connections."
    #print(type(value))
    result = get_name_and_number(value)
    if result != None:
        print(result)

def read_org():
    with open('organism-orig.csv', newline='') as csvfile:
        orgreader = csv.reader(csvfile, delimiter=',')
        for row in orgreader:
            process_row(row)

if __name__ == "__main__":
    read_org()
