from collections import defaultdict
import math

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        wordIndex = defaultdict(list)
        for i in range(0, len(words)):
            wordIndex[words[i]].append(i)

        # print wordIndex

        minDist = None
        for j in wordIndex[word1]:
            for k in wordIndex[word2]:
               minDist = abs(j-k) if minDist is None or abs(j-k)<minDist else minDist

        return minDist


if __name__ == '__main__':
    s = Solution()
    # print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    print s.shortestDistance(["coding", "practice", "makes", "perfect", "coding", "makes"], "coding", "makes")
