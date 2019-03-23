class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        individualsMap = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        pairsMap = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        output = 0
        i = 0
        while i < len(s):
            if s[i] == "I" or s[i] == "X" or s[i] == "C":
                if i+1 < len(s) and s[i]+s[i+1] in pairsMap:
                    output += pairsMap[s[i]+s[i+1]]
                    i += 2
                    continue
            if s[i] in individualsMap:
                output += individualsMap[s[i]]
                i += 1
        
        return output


if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("IV")
    print s.romanToInt("IX")
    print s.romanToInt("LVIII")
    print s.romanToInt("MCMXCIV")