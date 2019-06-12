class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        if len(strs) == 0:
            return output
        if len(strs) == 1:
            return strs[0]
        
        indexChar = {}
        for i in range(0, len(strs[0])):
            indexChar[i] = strs[0][i]
        
        maxPrefix = None
        for i in range(1, len(strs)):
            j = 0
            prefix = 0
            while j < len(strs[i]) and j in indexChar and strs[i][j] == indexChar[j]:
                prefix += 1
                j += 1
            maxPrefix = prefix if maxPrefix is None else min(prefix, maxPrefix)
        
        return strs[0][0:maxPrefix]

s = Solution()
print s.longestCommonPrefix(["flower","flow","flight"])