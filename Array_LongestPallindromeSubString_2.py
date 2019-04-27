from collections import defaultdict

class Solution(object):
    def checkIfPallindrome(self, arr):
        mid = len(arr)//2-1
        for i in range(0, mid+1):
            if arr[i] != arr[len(arr)-1-i]:
                return False
        return True
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        output = s[0]
        charIndex = defaultdict(list)
        for i in range(0, len(s)):
            charIndex[s[i]].append(i)
        
        if len(charIndex) == 1:
            return s
        
        for k, indexes in charIndex.items():
            if len(indexes) > 1:
                for i in range(0, len(indexes)-1):
                    for j in range(1, len(indexes)):
                        if indexes[j]-indexes[i]+1 > len(output) and self.checkIfPallindrome(s[indexes[i]:indexes[j]+1]):
                            output = s[indexes[i]:indexes[j]+1]
        return output
        
        
# from collections import defaultdict

# class Solution(object):
#     def checkIfPallindrome(self, arr):
#         mid = len(arr)//2-1
#         for i in range(0, mid+1):
#             if arr[i] != arr[len(arr)-1-i]:
#                 return False
#         return True
            
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) == 0:
#             return ""
#         output = s[0]
#         charIndex = defaultdict(list)
#         for i in range(0, len(s)):
#             if s[i] not in charIndex:
#                 charIndex[s[i]].append(i)
#             else:
#                 for index in charIndex[s[i]]:
#                     if len(s[index:i+1]) > len(output) and self.checkIfPallindrome(s[index:i+1]):
#                         output = s[index:i+1]
#                         break
#                 charIndex[s[i]].append(i)
#         return output
