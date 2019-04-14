from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        charIndex = defaultdict(list)
        output = s[0]
        for i in range(0, len(s)):
            if s[i] not in charIndex:
                charIndex[s[i]].append(i)
            else:
                for j in range(0, len(charIndex[s[i]])):
                    if i - charIndex[s[i]][j] + 1 > len(output):
                        fixStart = start = charIndex[s[i]][j]
                        fixEnd = end = i
                        isPallindrome = True
                        while start < end:
                            if s[start] != s[end]:
                                isPallindrome = False
                                break
                            start += 1
                            end -= 1

                        if isPallindrome:
                            output = s[fixStart : fixEnd + 1]
                charIndex[s[i]].append(i)

        return output

s = Solution()
print s.longestPalindrome("abadd")

