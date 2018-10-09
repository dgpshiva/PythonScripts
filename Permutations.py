def permute(input):
    if len(input) == 0:
        return

    if len(input) == 1:
        return [input]

    l = []

    for i in range(len(input)):
        m = input[i]
        rem = input[:i] + input[i+1:]
        for p in permute(rem):
            l.append([m] + p)

    return l

if __name__ == '__main__':
    input = ['A', 'B', 'C']
    print permute(input)

