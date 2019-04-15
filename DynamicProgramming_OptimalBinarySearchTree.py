import sys

def getSum(freq, start, end):
    return sum(freq[start : end+1])

def minCost(freq, n):
    cost = [[None for i in range(0, n)] for j in range(0, n)]

    for i in range(0, n):
        cost[i][i] = freq[i]
    
    for length in range(2, n+1):
        for i in range(0, n - length + 1):
            j = i + length - 1

            cost[i][j] = sys.maxint
            freqsSum = getSum(freq, i, j)

            for r in range(i, j+1):
                val = (cost[i][r-1] if r > i else 0) + (cost[r+1][j] if r < j else 0) + freqsSum

                cost[i][j] = val if val < cost[i][j] else cost[i][j]

    return cost[0][n-1]


keys = [10, 12, 20]
freq = [34, 8, 50]

print minCost(freq, 3)

