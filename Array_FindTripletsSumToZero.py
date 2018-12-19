class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[i] + nums[l] + nums[r] == 0:
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[l])
                        triplet.append(nums[r])
                        output.append(triplet)
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        l += 1
                    else:
                        r -= 1

        return output

s = Solution()
print s.threeSum([-1,0,1,2,-1,-4])

