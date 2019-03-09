from collections import defaultdict

class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        wordIndex = defaultdict(list)
        for i in range(0, len(words)):
            wordIndex[words[i]].append(i)

        minDist = None
        if word1 == word2:
            indexes = wordIndex[word1]
            indexes.sort()
            for i in range(0, len(indexes)-1):
                minDist = abs(indexes[i] - indexes[i+1]) if minDist is None or abs(indexes[i] - indexes[i+1]) < minDist else minDist

            return minDist
        else:
            indexesWord1 = sorted(wordIndex[word1])
            indexesWord2 = sorted(wordIndex[word2])
            indexWord1 = 0
            indexWord2 = 0
            while indexWord1 < len(indexesWord1) and indexWord2 < len(indexesWord2):
                minDist = abs(indexesWord1[indexWord1]-indexesWord2[indexWord2]) if minDist is None or abs(indexesWord1[indexWord1]-indexesWord2[indexWord2]) < minDist else minDist
                if indexesWord1[indexWord1] < indexesWord2[indexWord2]:
                    indexWord1 += 1
                else:
                    indexWord2 += 1

            return minDist


if __name__ == '__main__':
    s = Solution()
    # print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    print s.shortestWordDistance(["coding", "practice", "makes", "perfect", "coding", "makes"], "coding", "makes")
