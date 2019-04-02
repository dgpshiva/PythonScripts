from collections import deque
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = deque()
        count = 0
        i = len(S) - 1
        while i >= 0:
            if count < K:
                if S[i] == "-":
                    while i >= 0 and S[i] == "-":
                        i -= 1
                if i >= 0:
                    s.appendleft(S[i].upper())
                    count += 1
                    i -= 1
            else:
                if S[i] == "-":
                    while i >= 0 and S[i] == "-":
                        i -= 1
                if i >= 0:
                    s.appendleft("-")
                    count = 0

        return "".join(x for x in list(s))

if __name__ == '__main__':
    s = Solution()
    # print s.licenseKeyFormatting("2-4A0r7-4k", 3)
    print s.licenseKeyFormatting("--a-a-a-a--", 2)