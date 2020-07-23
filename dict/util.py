
import csv
import json

def dict_to_json(dict):
    myj = json.dumps(dict)
    print(myj)

def dict_to_csv(filename,dict,columns):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(columns)
        for key in dict.keys():
            ary = [key,dict[key]]
            csvwriter.writerow(ary)

if __name__ == "__main__":
    my_dict = {'aapl': 'apple', 'amzn': 'amazon', 'ui': 'ubiquiti'}
    my_columns = ['symbol','name']
    my_file = "dict.csv"

    dict_to_csv(my_file,my_dict,my_columns)
    dict_to_json(my_dict)
