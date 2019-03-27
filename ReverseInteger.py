# Reverse 32 bit signed integer
# If reversed number greater than 32 bit, return 0

import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Better solution from Leetcode 
        number = x
        rev = 0
        x = -x if x < 0 else x
        while x != 0:
            pop = int(x % 10)
            if x > 0 and rev > sys.maxint or (rev == sys.maxint and pop > 7):
                return 0
            if x < 0 and -rev < -sys.maxint-1 or (-rev == -sys.maxint-1 and pop < -8):
                return 0
            rev = rev * 10 + pop
            
            x = x // 10
        
        return rev if number > 0 else -rev


        # number = x
        # x = -x if x < 0 else x
        # digits = []
        # count = 0
        # output = 0
        # while x//10!=0:
        #     digits.append(x%10)
        #     x = x//10
        #     count += 1
        # if x > 0:
        #     digits.append(x)

        # for digit in digits:
        #     output += digit * pow(10, count)
        #     count -= 1

        # if output > pow(2, 31) - 1:
        #     return 0

        # output = -output if number < 0 else output

        # return output


if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(120)
    print s.reverse(-120)
    print s.reverse(1)
    print s.reverse(-1)
    print s.reverse(0)