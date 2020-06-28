import csv

def read_test():
    with open('ui-fun.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print(', '.join(row))

def write_test():
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['C1'] + ['C2'] + ['C3'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

if __name__ == "__main__":
    write_test()
