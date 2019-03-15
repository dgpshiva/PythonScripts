def minimumSwaps(arr):
    count = 0
    for i in range(0, len(arr)):
        while arr[i]-1 != i:
            index = arr[i]-1
            arr[i], arr[index] = arr[index], arr[i]
            count += 1
    return count


if __name__ == '__main__':
    #input = [4, 3, 1, 2]
    #input = [2, 3, 4, 1, 5]
    input = [1, 3, 5, 2, 4, 6, 7]
    print minimumSwaps(input)
