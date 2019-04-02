# Check if given integer is Pallindrome
# 321 - False
# 121 - True
# -121 - False (as reverse of it is 121-)
# 120 - False (as reverse of it is 21)
# Do not convert the integers to string

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers cannot be pallindrome
        # Number ending with 0 cannot be pallindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Find reverse of first half of the given number
        # Stopping point is when rev becomes greater than the number
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10

        # If number is of odd length like 12321
        # rev will be 123, so divide by 0 to eliminate middle number
        return x == rev or x == rev // 10


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(121)
    print s.isPalindrome(-121)
    print s.isPalindrome(321)
    print s.isPalindrome(0)
    print s.isPalindrome(120)
    print s.isPalindrome(-1)
