# People represented as integers are standing in a queue
# Each person can bribe at most 2 people
# Given final queue, find min bribes made to reach that state
# If more than 2 bribes have been made, return "Too chaotic"
# Eg: 2 1 5 3 4     -   min bribes made = 3 (2 by 5 and 1 by 2)


#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    minBribes = 0
    # Start from the end of the array
    for i in range(len(q)-1, -1, -1):
        # If current index of value is less than value-2, more than 2 bribes have been made
        # Eg:
        #   Index:  0 1 2 3 4
        #   Values: 1 5 2 3 4
        # 5 has made more than 2 bribes
        # If 5 had made exactly 2 bribes, his index would have been 2 ( 5 - 3)
        # If index is anything less than 2, he has made more than 2 bribes
        if q[i] - 3 > i:
            return "Too chaotic"

        # Count the number of people who have overtaken the current person
        # Eg:
        #   Index:      0 1 2 3 4
        #   Initial:    1 2 3 4 5
        #   Values:     1 4 2 3 5
        # Original position of 3 was 2
        # He was overtaken by 4 twice, so now 4 is at position 1
        # So, all people > 3 starting from 1 (3-2) to 3's current position have overtaken him
        # Add all these people to the count

        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                minBribes += 1

    return minBribes


if __name__ == '__main__':
    input = [2, 1, 5, 3, 4]
    minimumBribes(input)
