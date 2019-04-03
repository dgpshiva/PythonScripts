def findClosest(arr, value):
    if len(arr) == 0:
        return None

    if value <= arr[0]:
        return arr[0]
    if value >= arr[len(arr)-1]:
        return arr[len(arr)-1]

    mid = len(arr)//2
    if arr[mid] == value:
        return arr[mid]
    elif value < arr[mid]:
        if mid > 0 and value > arr[mid-1]:
            return arr[mid-1] if abs(arr[mid-1]-value) < abs(arr[mid]-value) else arr[mid]
        return findClosest(arr[0:mid], value)
    elif value > arr[mid]:
        if mid < len(arr) and value < arr[mid+1]:
            return arr[mid+1] if abs(arr[mid+1]-value) < abs(arr[mid]-value) else arr[mid]
        return findClosest(arr[mid:len(arr)], value)

if __name__ == '__main__':
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 4)
    print findClosest([2, 5, 6, 7, 8, 8, 9], 4)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 10)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 9)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 1)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 0)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], -1)
    print findClosest([1, 2, 4, 5, 6, 6, 8, 9], 7)
