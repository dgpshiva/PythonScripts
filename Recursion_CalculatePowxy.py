import math

# O(n) time complexity and O(1) space complexity
# def power(x, y):
#     if y == 0:
#         return 1

#     if int(y%2) == 0:
#         return power(x, y/2) * power(x, y/2)
#     else:
#         return x * power(x, y/2) * power(x, y/2)


# O(logn) time complexity
def power(x, y):
    if y == 0:
        return 1

    temp = power(x, int(y/2))

    if int(y%2) == 0:
        return temp * temp
    else:
        return x * temp * temp

print power(2, 3)
print 1.0/power(2, 3)
print math.pow(2, -3)
