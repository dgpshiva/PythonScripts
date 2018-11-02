def binarySearch(a, item):
    if len(a) == 0:
        return False

    middle = len(a)//2
    if a[middle] == item:
        return True
    elif item < a[middle]:
        return binarySearch(a[:middle], item)
    elif item > a[middle]:
        return binarySearch(a[middle+1:], item)


if __name__ == '__main__':
    a = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print binarySearch(a, 32)
    print binarySearch(a, 13)
    print binarySearch(a, 2)
    print binarySearch(a, 0)
    print binarySearch(a, 42)
    print binarySearch(a, 3)
