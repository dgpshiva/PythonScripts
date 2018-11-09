def mergeListsIntoNewList(listA, listB):
    output = []


    i = 0
    j = 0
    while i<len(listA) and j<len(listB):
        if listA[i] < listB[j]:
            output.append(listA[i])
            i += 1
        else:
            output.append(listB[j])
            j += 1

    if len(listA) == i:
        while j<len(listB):
            output.append(listB[j])
            j += 1
    else:
        while i<len(listA):
            output.append(listA[i])

    return output


if __name__ == '__main__':
    listA = [2, 5, 6]
    listB = [1, 3, 4, 7]

    print mergeListsIntoNewList(listA, listB)
