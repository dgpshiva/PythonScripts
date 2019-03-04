class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        output.append(1)

        for i in range(1, len(nums)):
            output.append(output[i-1] * nums[i-1])

        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print s.productExceptSelf(nums)
