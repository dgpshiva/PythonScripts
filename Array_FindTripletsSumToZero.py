def findTriplets(input):
    input.sort()
    s = set()
    output = []
    for i in range(0, len(input)-1):
        j = i+1
        k = len(input) - 1
        while j < k:
            if input[i] + input[j] + input[k] == 0:
                if str(input[i]) + ":" + str(input[j]) + ":" + str(input[k]) not in s:
                    triplet = []
                    triplet.append(input[i])
                    triplet.append(input[j])
                    triplet.append(input[k])
                    output.append(triplet)
                    s.add(str(input[i]) + ":" + str(input[j]) + ":" + str(input[k]))
                j += 1
                k -= 1
            elif input[i] + input[j] + input[k] < 0:
                j += 1
            else:
                k -= 1

    return output


if __name__ == '__main__':
    print findTriplets([-1, 0, 1, 2, -1, -4])

