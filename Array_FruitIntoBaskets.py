class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        maxCount = None
        basketOneCurrent = tree[0]
        basketTwoCurrent = None
        switchIndex = None
        switchMade = False
        count = 0
        i = 0
        while i < len(tree):
            if tree[i] == basketOneCurrent or tree[i] == basketTwoCurrent:
                count += 1
                i += 1
            elif tree[i] != basketOneCurrent and tree[i] !=  basketTwoCurrent and not switchMade:
                basketTwoCurrent = tree[i]
                count += 1
                switchIndex = i
                switchMade = True
                i += 1
            elif tree[i] != basketOneCurrent and tree[i] !=  basketTwoCurrent and switchMade:
                maxCount = count if maxCount is None or count > maxCount else maxCount
                basketOneCurrent = tree[switchIndex]
                basketTwoCurrent = None
                count = 0
                i = switchIndex
                switchMade = False
                
        
        output = count if maxCount is None or count > maxCount else maxCount
        return output