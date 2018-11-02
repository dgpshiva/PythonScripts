def containsPairWithSum(input, sum):
   s = set()

   for i in input:
        temp = sum - i
        if temp > 0 and temp in s:
           print (i, temp)
        s.add(i)

if __name__ == '__main__':
    A = [1,4,45,6,10,8]
    containsPairWithSum(A, 16)
