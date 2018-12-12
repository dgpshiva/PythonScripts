def search(input, first, last, value):
    if last < first:
        return -1

    mid = (first+last)//2

    if input[mid] == value:
        return mid
    elif input[first] < input[mid]:
        if value >= input[first] and value <= input[mid]:
            return search(input, first, mid-1, value)
        else:
            search(input, mid+1, last, value)
    elif input[first] > input[mid]:
        if value >= input[mid] and value <= input[last]:
            return search(input, mid+1, last, value)
        else:
            return search(input, first, mid-1, value)
    else:
        if input[mid] != input[last]:
            return search(input, mid+1, last, value)
        else:
            result = search(input, first, mid-1, value)
            if result == -1:
                return search(input, mid+1, last, value)
            return result


if __name__ == '__main__':
    input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print search(input, 0, len(input)-1, 5)




