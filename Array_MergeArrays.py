def mergeLists(listA, listB, noOfElementInA, noOfElementsInB):
    lastA = noOfElementInA - 1
    lastB = noOfElementsInB - 1
    lastMerged = noOfElementInA + noOfElementsInB - 1

    while lastB >= 0:
        if lastA >= 0 and listA[lastA] > listB[lastB]:
            listA[lastMerged] = listA[lastA]
            lastA -= 1
        else:
            listA[lastMerged] = listB[lastB]
            lastB -= 1

        lastMerged -= 1

    return listA


if __name__ == '__main__':
    listA = [1, 3, 6, 7, -1, -1, -1, -1, -1]
    listB = [2, 4, 5, 8, 9]
    print mergeLists(listA, listB, 4, 5)
