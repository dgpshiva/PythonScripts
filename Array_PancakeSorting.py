def findIndexOfMax(arr, n):
    maxIndex = 0
    for i in range(0, n):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    
    return maxIndex


def flip(arr, i):
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1
    

def pancakeSort(arr, n):
    curSize = n
    while curSize > 1:
        mi = findIndexOfMax(arr, curSize)
        if mi != curSize-1:
            flip(arr, mi)
            print arr
            flip(arr, curSize-1)
            print arr
            print mi+curSize+1
    
        curSize -= 1

    return arr

print pancakeSort([3, 2, 4, 1], 4)
