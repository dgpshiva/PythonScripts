def SeiveOfErathosthenes(input):
    prime = [True for i in range(input+1)]

    p = 2
    while p*p <= input:
        if prime[p]:
            for i in range(p*2, input+1, p):
                prime[i] = False
        p += 1

    for i in range(2, input+1):
        if prime[i]:
            print str(i) + " ",


if __name__ == '__main__':
    # SeiveOfErathosthenes(20)
    SeiveOfErathosthenes(13)
