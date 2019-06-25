from collections import defaultdict

def findSecondMostFreqChar(inputString):
    maxCount = 0
    charCount = {}
    countChar = defaultdict(list)

    for c in inputString:
        if c not in charCount:
            charCount[c] = 1
        else:
            charCount[c] += 1
        maxCount = max(maxCount, charCount[c])
    
    for char, count in charCount.iteritems():
        countChar[count].append(char)
    
    for i in range(maxCount-1, -1, -1):
        if i in countChar:
            return countChar[i]


if __name__ == '__main__':
    print findSecondMostFreqChar("banananx")