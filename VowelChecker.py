from collections import defaultdict
import re

# Beautiful solution
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        words = {w : w for w in wordlist}
        caps = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", "#", w.lower()): w for w in wordlist[::-1]}
        return [words.get(w) or caps.get(w.lower()) or vowel.get(re.sub("[aeiou]", "#", w.lower())) or "" for w in queries ]



# class Solution(object):
#     def spellchecker(self, wordlist, queries):
#         """
#         :type wordlist: List[str]
#         :type queries: List[str]
#         :rtype: List[str]
#         """

#         answer = []

#         vowelsSet = set()
#         vowelsSet.add('a')
#         vowelsSet.add('e')
#         vowelsSet.add('i')
#         vowelsSet.add('o')
#         vowelsSet.add('u')

#         s = set()
#         lowerList = []
#         nonVowelDictList = []

#         for word in wordlist:
#             s.add(word)
#             lowerList.append(word.lower())

#             nonVowelDict = defaultdict(list)
#             for i in range(0, len(word)):
#                 cLower = word[i].lower()
#                 if cLower not in vowelsSet:
#                     nonVowelDict[cLower].append(i)
#             nonVowelDictList.append(nonVowelDict)

#         for query in queries:
#             if query in s:
#                 answer.append(query)
#                 continue

#             foundLower = False
#             for i in range(0, len(lowerList)):
#                 if query.lower() == lowerList[i]:
#                     answer.append(wordlist[i])
#                     foundLower = True
#                     break

#             if foundLower:
#                 continue

#             queryNonVowelDict = defaultdict(list)
#             for j in range(0, len(query)):
#                 cLower = query[j].lower()
#                 if cLower not in vowelsSet:
#                     queryNonVowelDict[cLower].append(j)
#             foundVowelErr = False
#             for i in range(0, len(nonVowelDictList)):
#                 if nonVowelDictList[i] == queryNonVowelDict:
#                     answer.append(wordlist[i])
#                     foundVowelErr = True
#                     break

#             if foundVowelErr:
#                 continue

#             answer.append("")

#         return answer



if __name__ == '__main__':
    s = Solution()
    print s.spellchecker(["KiTe","kite","hare","Hare"],
                            ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
