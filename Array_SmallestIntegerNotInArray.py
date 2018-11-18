# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    s = set()

    for i in A:
        if i > 0:
            s.add(i)

    if len(s) == 0:
        return 1
    else:
        currentValue = 1
        while currentValue in s:
            currentValue += 1
        return currentValue
