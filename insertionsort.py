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
#In some particular cases, we shall be interested in the average-case running time of an algorithm; we shall see the technique of probabilistic analysis applied to various algorithms throughout this book. The scope of average-case analysis is limited, because it may not be apparent what constitutes an “average” input for a particular problem. Often, we shall assume that all inputs of a given size are equally likely. In practice, this assumption may be violated, but we can sometimes use a randomized algorithm, which makes random choices, to allow a probabilistic analysis and yield an expected running time. We explore randomized algorithms more in Chapter 5 and in several other subsequent chapters.
