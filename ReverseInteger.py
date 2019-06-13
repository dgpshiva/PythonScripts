# Reverse 32 bit signed integer
# If reversed number greater than 32 bit, return 0

import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Working solution from Leetcode
        number = x
        x = -x if x < 0 else x
        
        rev = 0
        while x != 0:
            rev = rev * 10 + (x%10)
            x = x//10
        
        if number > 0 and rev > pow(2, 31) - 1:
            return 0
        if number < 0 and -rev < -pow(2, 31):
            return 0
        
        return -x if number < 0 else x


        # Better solution from Leetcode BUT Does not pass all Leetcode tests
        # number = x
        # rev = 0
        # x = -x if x < 0 else x
        # while x != 0:
        #     pop = int(x % 10)
        #     if x > 0 and rev > sys.maxint or (rev == sys.maxint and pop > 7):
        #         return 0
        #     if x < 0 and -rev < -sys.maxint-1 or (-rev == -sys.maxint-1 and pop < -8):
        #         return 0
        #     rev = rev * 10 + pop
            
        #     x = x // 10
        
        # return rev if number > 0 else -rev

        
if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(120)
    print s.reverse(-120)
    print s.reverse(1)
    print s.reverse(-1)
    print s.reverse(0)