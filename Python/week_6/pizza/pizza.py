import sys
import os
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        name = sys.argv[1]
        if not name.endswith('.csv'):
            sys.exit('Not a CSV file')
        if not os.path.isfile(name):
            sys.exit('File does not exist')

        table = []
        with open(name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)

        print(tabulate(table, headers='firstrow', tablefmt='grid'))


if __name__ == '__main__':
    main()
