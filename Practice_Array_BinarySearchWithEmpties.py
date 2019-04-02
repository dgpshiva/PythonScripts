# def binarySearch(input, first, last, value):
def binarySearch(input, value):
    if not input:
        return None

    # if first > last:
    #     return None
    first = 0
    last = len(input) - 1
    mid = (first+last)//2
    if input[mid] == "":
        left = mid - 1
        right = mid + 1

        while left >= first and right <= last:
            if input[left] != "":
                mid = left
                break
            if input[right] != "":
                mid = right
                break
            left += 1
            right -= 1

        if input[mid] == value:
            return input[mid]
        if input[mid] < value:
            # first = mid + 1
            # return binarySearch(input, first, last, value)
            return binarySearch(input[mid+1 : last+1], value)
        else:
            # last = mid - 1
            # return binarySearch(input, first, last, value)
            return binarySearch(input[first : mid], value)


if __name__ == '__main__':
    input = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    # print binarySearch(input, 0, len(input)-1, "ball")
    # print binarySearch(input, 0, len(input)-1, "")
    print binarySearch(input, "ball")
    print binarySearch(input, "cat")
    # print binarySearch(input, "")
    print binarySearch(input, "at")

