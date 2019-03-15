#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = None
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[0])-2):
            currentSum = returnHourGlassSum(arr, i, j)
            maxSum = currentSum if maxSum is None or currentSum > maxSum else maxSum
    return maxSum

def returnHourGlassSum(arr, i, j):
    sum = 0
    for m in range(i, i+3):
        for n in range(j, j+3):
            sum += arr[m][n]
    return sum - arr[i+1][j] - arr[i+1][j+2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
