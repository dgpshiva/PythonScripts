def returnNumbers(N, K):
    output = []

    if N == 0:
        return output

    if N == 1:
        output.append(0)

    DFS(N, K, output, 0)

    return output


def DFS(N, K, output, number):
    if N == 0:
        output.append(number)
        return

    for i in range(0, 10):
        if i == 0 and number == 0:
            continue

        elif number == 0 and i != 0:
            DFS(N-1, K, output, i)

        elif abs((number%10) - i) == K:
            DFS(N-1, K, output, number*10 + i)



if __name__ == '__main__':
    # print returnNumbers(2, 1)
    # print returnNumbers(3, 2)
    print returnNumbers(1, 2)
