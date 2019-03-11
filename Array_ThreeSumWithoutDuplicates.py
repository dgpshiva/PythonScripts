class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                l = i+1
                r = len(nums)-1
                while l < r:
                    if nums[l]+nums[r]+nums[i] == 0:
                        output.append([nums[l], nums[r], nums[i]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]+nums[i]<0:
                        l+=1
                    elif nums[l]+nums[r]+nums[i]>0:
                        r-=1

        return output


if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])