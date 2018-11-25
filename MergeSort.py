def mergeSort(input):
    if len(input) > 1:
        mid = len(input)//2
        leftHalf = input[:mid]
        rightHalf = input[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                input[k] = leftHalf[i]
                i += 1
            else:
                input[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            input[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            input[k] = rightHalf[j]
            j += 1
            k += 1

        return input


if __name__ == '__main__':
    input = [5, 2, 9, 8, 3]
    print mergeSort(input)
