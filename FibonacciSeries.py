# Using Recursion
# Exponential and O(n) call stack

# def fibonacci(n):
#     if n < 0:
#         return "Incorrect input"
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print fibonacci(9)



# Using Recursion but storing previously computed values
# O(n) time and O(n) space complexity

# def fibonacci(n):
#     FibArray = [0, 1]

#     while len(FibArray) < n+1:
#         FibArray.append(0)

#     if n <= 1:
#         return n
#     else:
#         if FibArray[n-1] == 0:
#             FibArray[n-1] = fibonacci(n-1)
#         if FibArray[n-2] == 0:
#             FibArray[n-2] = fibonacci(n-2)
#         FibArray[n] = FibArray[n-1] + FibArray[n-2]
#     return FibArray[n]

# print fibonacci(9)



# Using loops
# O(n) time complexity and O(1) space complexity

# def fibonacci(n):
#     if n < 0:
#         return "Incorrect input"

#     a = 0
#     b = 1

#     if n == 1:
#         return a
#     if n == 2:
#         return b

#     i = 3
#     while i <= n:
#         c = a + b
#         a = b
#         b = c
#         i += 1
#     return c

# print fibonacci(9)



# Using mathematical formulae
# O(logn) time complecity and O(1) space complexity

MAX = 1000
f = [0] * MAX
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    if f[n]:
        return f[n]

    if n&1:
        k = (n+1)//2
    else:
        k = n//2

    if n&1:
        f[n] = fib(k) * fib(k) + fib(k-1) * fib(k-1)
    else:
        f[n] = (2*fib(k-1) + fib(k)) * fib(k)

    return f[n]

print fib(9)
