# Perform binary search in array of strings that may have empty strings
# Eg. input: ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

def binarySearch(input, value):
    if not input:
        return None

    first = 0
    last = len(input) - 1
    mid = (first+last)//2

    # If mid value is an empty string, 
    # find the immediate left or right non-empty value
    # and set mid to that
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
            return binarySearch(input[mid+1 : last+1], value)
        else:
            return binarySearch(input[first : mid], value)


if __name__ == '__main__':
    input = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print binarySearch(input, "ball")
    print binarySearch(input, "cat")
    print binarySearch(input, "")
    print binarySearch(input, "at")
   