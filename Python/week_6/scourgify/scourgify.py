import sys
import os
import csv

def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        i_file = sys.argv[1]
        o_file = sys.argv[2]
        if not i_file.endswith('.csv'):
            sys.exit('Not a CSV file')
        if not os.path.isfile(i_file):
            sys.exit('File does not exist')

        with open(i_file, 'r') as file:
            reader = csv.DictReader(file)
            data = []

            for row in reader:
                name = row['name']
                house = row['house']
                last, first = name.split(' ')
                last = last.replace(',','')
                data.append({'first': first, 'last': last, 'house': house})

        with open(o_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'], delimiter=' ', quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    main()
