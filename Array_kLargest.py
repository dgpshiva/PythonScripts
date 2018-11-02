def returnKLargest(input, k):
    input.sort(reverse=True)
    return input[:3]

if __name__ == '__main__':
    input = [1, 23, 12, 9, 30, 2, 50]

    print returnKLargest(input, 3)
