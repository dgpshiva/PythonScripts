class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        s1 = set()
        s2 = set()

        for num in nums1:
            s1.add(num)
        for num in nums2:
            s2.add(num)

        return s1.intersection(s2)



if __name__ == '__main__':
    s = Solution()
    # print s.intersection([1,2,2,1], [2,2])
    print s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
