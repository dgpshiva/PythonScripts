class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # n = len(nums)
        # count = 0
        # while not self.checkIfEqual(nums):
        #     count += 1
        #     nums.sort()
        #     nums[:n-1] = [x+1 for x in nums[:n-1]]
        # return count

        # Better solution from Leetcode
        return sum(nums) - min(nums)*len(nums)

    def checkIfEqual(self, nums):
        return nums[1:] == nums[:-1]


if __name__ == '__main__':
    s = Solution()
    print s.minMoves([1, 2, 3])
