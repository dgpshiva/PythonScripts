def quickSort(input):
    quickSortHelper(input, 0, len(input)-1)

def quickSortHelper(input, first, last):
    if first < last:
        splitPoint = partition(input, first, last)
        quickSortHelper(input, first, splitPoint-1)
        quickSortHelper(input, splitPoint+1, last)

def partition(input, first, last):
    pivot = input[first]
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        while leftMark <= rightMark and input[leftMark] <= pivot:
            leftMark += 1
        while input[rightMark] >= pivot and rightMark >= leftMark:
            rightMark -= 1

        if rightMark < leftMark:
            done = True
        else:
            temp = input[leftMark]
            input[leftMark] = input[rightMark]
            input[rightMark] = temp

    temp = input[first]
    input[first] = input[rightMark]
    input[rightMark] = temp

    return rightMark



if __name__ == '__main__':
    input = [5, 2, 9, 8, 3]

    quickSort(input)

    print input
