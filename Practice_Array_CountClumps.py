def countClumps(arr):
    if len(arr) == 1:
        return 0
    clumpsCount = 0
    current = arr[0]
    currentCount = 0
    for i in range(0, len(arr)):
        if arr[i] == current:
            currentCount += 1
        else:
            if currentCount > 1:
                clumpsCount += 1
            current = arr[i]
            currentCount = 1
    return clumpsCount + 1 if currentCount > 1 else clumpsCount

if __name__ == '__main__':
    print countClumps([1, 2, 2, 3, 4, 4])   # Expectd output: 2
    print countClumps([1, 1, 2, 1, 1])  # Expectd output: 2
    print countClumps([1, 1, 1, 1, 1])  # Expectd output: 1
    print countClumps([1, 2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 2, 2, 3])  # Expectd output: 1
    print countClumps([2, 3, 3])  # Expectd output: 1
    print countClumps([2, 3])  # Expectd output: 0
    print countClumps([2])  # Expectd output: 0


