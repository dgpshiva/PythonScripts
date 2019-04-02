def checkIfPythagoreanTripletExists(arr):
    arr.sort()
    for i in range(len(arr)-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if arr[j]**2 + arr[k]**2 == arr[i]**2:
                return [arr[i], arr[j], arr[k]]
            if arr[j]**2 + arr[k]**2 > arr[i]**2:
                k = k -1
            else:
                j = j + 1

    return None


if __name__ == '__main__':
    # input = [3, 1, 4, 6, 5]
    input = [10, 4, 6, 12, 5]
    print checkIfPythagoreanTripletExists(input)