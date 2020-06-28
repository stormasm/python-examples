import csv

def read_test():
    with open('ui-fun.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

def write_csv1(index,symbol,dyield,payout):
    with open('eggs1.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['index'] + ['symbol'] + ['yield'] + ['payout'])
        spamwriter.writerow([index,symbol,dyield,payout])

def write_csv2(data):
    with open('eggs2.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['index'] + ['symbol'] + ['yield'] + ['payout'])
        for row in data:
            spamwriter.writerow([row[0]] + [row[1]] + [row[2]] + [row[3]])

def write_test_1():
    c1 = "1"
    c2 = "ui"
    c3 = "1.1"
    c4 = "10%"
    write_csv1(c1,c2,c3,c4)

def write_test_2():
    arr = []
    a1 = ['1','2','3','4']
    arr.append(a1)
    a2 = ['11','12','13','14']
    arr.append(a2)
    a3 = ['21','22','23','24']
    arr.append(a3)
    write_csv2(arr)

if __name__ == "__main__":
    write_test_2()
