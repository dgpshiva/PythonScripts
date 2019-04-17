# Find the length of longest sub string inside given string that does not have repeating characters
# Eg: abcabcbb  Ans: 3 (abc)
#   "bbbbb"     Ans: 1 (b)
#   "pwwkew"    Ans: 3 (wke)

# Normal sliding window solution
# def returnLongestCount(s):
#     first = 0
#     runner = 0
#     charsSet= set()
#     maxCount = 0

#     while first < len(s) and runner < len(s):
#         if s[runner] not in charsSet:
#             maxCount = max(maxCount, runner - last + 1)
#             charsSet.add(s[runner])
#             runner += 1
#         else:
#             charsSet.remove(s[first])
#             first += 1

#     return maxCount


# Optimized sliding window solution
def returnLongestCount(s):
    first = 0
    runner = 0
    charIndex = {}
    maxCount = 0

    while runner < len(s):
        if s[runner] in charIndex:
            first = max(first, charIndex[s[runner]])
        maxCount = max(maxCount, runner - first + 1)
        charIndex[s[runner]] = runner + 1
        runner += 1

    return maxCount


print returnLongestCount("pwwkew")