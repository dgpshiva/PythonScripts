def search(input, first, last, toSearch):
    if first > last:
        return -1

    mid = (first+last)//2
    if input[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if first > left and right > last:
                return -1
            if first <= left and input[left] != "":
                mid = left
                break
            if right <= last and input[right] != "":
                mid = right
                break
            left -= 1
            right += 1

    if input[mid] == toSearch:
        return mid
    elif toSearch > input[mid]:
        return search(input, mid+1, last, toSearch)
    else:
        return search(input, first, mid-1, toSearch)


if __name__ == '__main__':
    input = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print search(input, 0, len(input), "ball")
