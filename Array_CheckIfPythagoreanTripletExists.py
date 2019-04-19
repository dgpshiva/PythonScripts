# Given and array of integers, check if a triplet a, b, c exists,
# such that a^2 + b^2 = c^2

def pythagoreanTripletExists(input):
    # Square all the numbers and sort them
    squaredList = [i ** 2 for i in input]
    squaredList.sort()

    # Now that array is sorted, we know hypotnuse will exist in the right end
    # Iterate from right end of array
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
