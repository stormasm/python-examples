
import csv

my_dict = {'aapl': 'apple', 'amzn': 'amazon', 'ui': 'ubiquiti'}

my_columns = ['symbol','name']

csv_file = "dict.csv"

with open(csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(my_columns)
    for key in my_dict.keys():
        ary = [key,my_dict[key]]
        csvwriter.writerow(ary)
