#!/usr/bin/env python
"""
Elements of programming interviews . com
"""
import csv
import json

def readcsv(file_):
    """Read the given csv file
    """
    #extract the open price
    S = list()
    with open(file_) as csvfile:
        prices_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in prices_reader:
            S.append(row[1])
    S = S[1:]
    return S


def csv_to_json(csvfile, jsonfile):
    """
    Read a csv file into a json file
    """
    fieldnames = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close')
    reader = None
    with open(csvfile, 'r') as csvf:
        with open(jsonfile, 'w') as jsonf:
            reader = csv.DictReader( csvf, fieldnames )
            for row in reader:
                json.dump(row, jsonf)
                jsonf.write('\n')

if __name__ == '__main__':
    S = readcsv('table.csv')
    # Divide and conquer algorithm
    # Partition the list and solve each partition
    # Difficult part is to combine the results

    # more elegant algorithm
    m = float(S[0])
    d = 0
    d_now = 0
    for i in xrange(1, len(S), 1):
        if float(S[i]) < m:
            m = float(S[i])
        else:
            d_now = float(S[i]) - m
        if d_now > d:
            d = d_now
    print("max profit", d)
