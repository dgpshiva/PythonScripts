class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        while not self.checkIfEqual(nums):
            count += 1
            sorted(nums)
            nums[:n-1] = [x+1 for x in nums[:n-1]]
        return count

    def checkIfEqual(self, nums):
        return nums[1:] == nums[:-1]