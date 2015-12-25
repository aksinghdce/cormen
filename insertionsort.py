#!/usr/bin/env python
def insertionsort():
    """insertion sort on a list"""
    data = [2,12,1,0,-1,15,17,0]
    for j in xrange(1, len(data), 1):
        key = data[j]
        i = j - 1
        while i > -1 and data[i] > key:
            data[i+1] = data[i]
            i = i - 1
        data[i+1] = key
    return data


if __name__ == '__main__':
    sorted_data = insertionsort()
    print(sorted_data)
    
#Result: [-1, 0, 0, 1, 2, 12, 15, 17]
#Best case: array is already sorted: O(n)
#Worst case: array is reversed sorted : O(n^2)
