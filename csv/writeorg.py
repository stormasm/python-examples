import csv
import re


def get_name_and_number(input):
    m = re.match(
        r"(?P<x0>Organism) (?P<x1>\w+) (?P<x2>\w+) (?P<x3>has) (?P<x4>\d+)", input
    )
    if m == None:
        return None
    r1 = m.group("x1") + " " + m.group("x2")
    r2 = m.group("x4")
    mytuple = (r1, r2)
    return mytuple


def process_row(row):
    result = get_name_and_number(row[1])
    if result != None:
        print(result)
        print(row[2])


def write_org(data):
    with open("organism.csv", "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",")
        spamwriter.writerow(["index"] + ["name"] + ["numproteins"] + ["link"])
        for row in data:
            spamwriter.writerow([row[0]] + [row[1]] + [row[2]] + [row[3]])

def read_org():
    with open("organism-orig.csv", newline="") as csvfile:
        orgreader = csv.reader(csvfile, delimiter=",")
        for row in orgreader:
            process_row(row)

def write_test():
    arr = []
    a1 = ["1", "2", "3", "4"]
    arr.append(a1)
    a2 = ["11", "12", "13", "14"]
    arr.append(a2)
    a3 = ["21", "22", "23", "24"]
    arr.append(a3)
    write_org(arr)

if __name__ == "__main__":
    #read_org()
    write_test()
