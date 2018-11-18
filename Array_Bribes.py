#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    minBribes = 0

    for i in range(len(q)-1, -1, -1):
        if q[i] - (i+1) > 2:
            print "Too chaotic"
            return
        for j in range(max(0, q[i]-2, i)):
            if q[j] > q[i]:
                minBribes += 1

    print minBribes


if __name__ == '__main__':
    input = [2, 1, 5, 3, 4]
    minimumBribes(input)
