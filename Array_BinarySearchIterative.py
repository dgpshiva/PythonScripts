def binarySearch(a, item):
    first = 0
    last = len(a) - 1

    while first <= last:
        middle = (first + last)//2  # Double back slash means floor division. This is cool!!

        if a[middle] == item:
            return True
        elif item > a[middle]:
            first = middle + 1
        elif item < a[middle]:
            last = middle - 1

    return False


if __name__ == '__main__':
    a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print binarySearch(a, 32)
    print binarySearch(a, 13)
    print binarySearch(a, 2)
    print binarySearch(a, 0)
    print binarySearch(a, 42)
    print binarySearch(a, 3)
