def sortElements(input):
    arr = [None] * 11

    for el in input:
        arr[el] = el

    return arr


if __name__ == '__main__':
    input = [3, 6, 1, 9, 10]

    print sortElements(input)
