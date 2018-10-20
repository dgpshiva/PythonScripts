def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def GCDOfList(num, arr):
    if num == 0:
        return None
    if num == 1:
        return arr[0]

    num1 = arr[0]
    num2 = arr[1]
    gcd = GCD(num1, num2)
    for i in range(2, num):
        gcd = GCD(gcd, arr[i])

    return gcd

# print GCDOfList(5, [2, 4, 6, 8, 16])
# print GCDOfList(4, [4, 6, 8, 16])
print GCDOfList(4, [2, 3, 4, 5])
