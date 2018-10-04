def pythagoreanTripletExists(input):
    squaredList = [i ** 2 for i in input]
    squaredList.sort()

    for i in range(len(squaredList)-1, 1, -1):
        hypotnuse = squaredList[i]

        j = 0
        k = i - 1
        while j<k:
            if squaredList[j] + squaredList[k] == hypotnuse:
                return True
            elif squaredList[j] + squaredList[k] > hypotnuse:
                k = k - 1
            else:
                j = j + 1

    return False


if __name__ == '__main__':
    ar = [3, 1, 4, 6, 5]
    # ar = [10, 4, 6, 12, 5]
    print pythagoreanTripletExists(ar)
