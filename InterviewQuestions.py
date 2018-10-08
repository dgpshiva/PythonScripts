# Question 1
# T = (0.1, 0.1)
# x = 0.0
# for i in range(len(T)):
#     for j in T:
#         x += i + j
#         print x
# print i

# Question 2
# def f(s):
#     if len(s) <= 1:
#         return s
#     return f(f(s[1:])) + s[0]
# print f('mat')
# print f('math')

# Question 3
# import random
# tots = [0.00] * 3
# maxVals = [0.0] * 3
# mean = 100.0
# stdDevs = [0.0, 20.0, 40.0]
# for i in range(1000):
#     for j in range(len(tots)):
#         nextVal = random.gauss(mean, stdDevs[j])
#         tots[j] += nextVal
#         if nextVal > maxVals[j]:
#             maxVals[j] = nextVal
# print tots

# Question 4
# def Foo(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
# a = Foo(5)
# b = Foo(5)
# print a(b(2))

# Question 5
def make_pretty(func):
    def inner():
        print "I got decorated"
        func()
    return inner

def ordinary():
    print "I am ordinary"

pretty = make_pretty(ordinary)
pretty()

