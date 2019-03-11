class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(0, len(nums)-1):
            s = set()
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in s:
                    output.append([nums[i], nums[j], -(nums[i]+nums[j])])
                s.add(nums[j])

        return output


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
