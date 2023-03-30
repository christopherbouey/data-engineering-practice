import boto3
import glob
import json
import csv

def flatten(y):
    out = {}
 
    def flatten(x, name=''):
 
        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:
 
            for a in x:
                flatten(x[a], name + a + '_')
 
        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:
 
            i = 0
 
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
 
    flatten(y)
    return out

def get_json():
    return glob.glob('data/**/*.json', recursive=True)

def main():
    json_files = get_json()
    for file in json_files:
        print(file)
        # Open json file and store data
        json_file = open(file)
        data = json.load(json_file)
        flattened_data = flatten(data)
        data_keys = list(flattened_data.keys())
        data_values = list(flattened_data.values())

        # Create CSV file and load in json header and values
        with open(file[:-5] + '.csv', 'w', encoding='utf8') as csv_file:
            print('File opened')
            #Create writer
            csv_write = csv.writer(csv_file)
            # Write header
            csv_write.writerow(data_keys)
            csv_write.writerow(data_values)


if __name__ == '__main__':
    main()
