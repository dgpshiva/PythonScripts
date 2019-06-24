class Solution(object):
    
    def __init__(self):
        self.totalCount = 0
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0 and s[0] >= 1:
            self.numDecodingsUtil(s[1:len(s)])
            self.totalCount += 1
        if len(s) > 1 and int(s[0]+s[1]) >= 10 and int(s[0]+s[1]) <= 26:
            # print int(s[0]+s[1])
            self.numDecodingsUtil(s[2:len(s)])
            self.totalCount += 1
        return self.totalCount
        
    def numDecodingsUtil(self, s):
        if len(s) > 1:
            valid = True
            i = 0
            while i < len(s)-1:
                # print int(s[i]+s[i+1])
                if int(s[i]+s[i+1]) < 10 or int(s[i]+s[i+1]) > 26:
                    valid = False
                    break
                else: 
                    i += 2
            if valid and i == len(s)-1:
                if s[i] < 1:
                    valid = False
            if valid:
                self.totalCount += 1

            if s[0] >= 1:
                self.numDecodingsUtil(s[1:len(s)])


if __name__ == "__main__":
    s = Solution()
    # print s.numDecodings("12")
    # print s.numDecodings("226")
    print s.numDecodings("22116")