def rotLeft(a, d):
    n = d%len(a)
    arr = a+a
    end = len(arr)-(len(a)-n)
    return arr[n:end]

print rotLeft([1, 2, 3, 4, 5], 2)