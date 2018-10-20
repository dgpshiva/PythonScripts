def GCD(x, y):
    while y:
        x, y = y, x % y

    return x


print GCD(210, 45)

