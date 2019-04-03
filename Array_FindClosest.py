# Given a number, find element closest to it in an array
# Efficient solution:
#   -   Check edge cases, if element lower than least ot greater than greatest,
#       return least and greatest respectively
#   -   Perform binary search
#   -   If number == arr[mid], return arr[mid]
#   -   else if number < arr[mid]
#           if number > arr[mid-1], return arr[mid] or arr[mid-1], whichever is closest
#           else continue with binary search
#   -   else if number > arr[mid]
#           if number < arr[mid+1], return arr[mid] or arr[mid+1], whichever is closest
#           else continue with binary search


def findClosest(arr, target):
    arr.sort()

    if target <= arr[0]:
        return arr[0]
    if target >= arr[len(arr)-1]:
        return arr[len(arr)-1]

    i = 0
    j = len(arr)-1

    while i<j:
        mid = (i+j)//2
        if arr[mid] == target:
            return arr[mid]
        elif target < arr[mid]:
            if mid>0 and target > arr[mid-1]:
                return getClosest(arr, mid-1, mid, target)
            j = mid-1
        else:
            if mid<len(arr) and target < arr[mid+1]:
                return getClosest(arr, mid, mid+1, target)
            i = mid+1

    return -1

def getClosest(arr, first, second, target):
    return arr[first] if abs(arr[first]-target)<abs(arr[second]-target) else arr[second]


if __name__ == '__main__':
    # arr = [1, 2, 4, 5, 6, 6, 8, 9]
    arr = [2, 5, 6, 7, 8, 8, 9]

    print findClosest(arr, 4)
