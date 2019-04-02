def minBribes(q):
    count = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - 3 > i:
            return "Too chaotic"
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                count += 1

    return count

if __name__ == '__main__':
    input = [2, 1, 5, 3, 4]
    print minBribes(input)
