# Need to find what this does, else delete

def findConsequitiveNumbers(N):
    ans = 0
    for k in range(1, 2*N+1):
        if 2*N % k == 0:
            y = 2*N/k - k - 1
            if y%2 == 0 and y>=0:
                ans += 1

    return ans

print findConsequitiveNumbers(5)
