def pythagoreanTripletExists(input):
    squaredList = [i ** 2 for i in input]
    squaredList.sort()

    s = set()
    for i in range(len(squaredList)-1, -1, -1):
        if i == len(squaredList)-1:
            hypotnuse = squaredList[i]
        else:
            temp = hypotnuse - squaredList[i]
            if temp > 0 and temp in s:
                return True
            s.add(squaredList[i])

    return False


if __name__ == '__main__':
    ar = [3, 1, 4, 6, 5]
    print pythagoreanTripletExists(ar)
