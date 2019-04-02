class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = cur = 0
        i = 0
        for j in range(0, len(A)):
            res = max(res, cur + A[j])
            if A[i] + i - (j+1) < A[j] + j - (j+1):
                i = j
                cur = A[i] + i - (j+1)
            else:
                cur = A[i] + i - (j+1)

        return res


if __name__ == '__main__':
    s = Solution()
    print s.maxScoreSightseeingPair([8, 1, 5, 2, 6])
