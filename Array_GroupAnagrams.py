from collections import defaultdict

def groupAnagrams(input):
    sortedWordAnagrams = defaultdict(list)

    for item in input:
        itemList = list(item)
        itemList.sort()
        key = ''.join(itemList)
        sortedWordAnagrams[key].append(item)

    output = []
    for valuesList in sortedWordAnagrams.itervalues():
        for value in valuesList:
            output.append(value)

    return output


if __name__ == '__main__':
    input = ["shiva", "nivi", "vini", "hisav", "test", "etst", "sett", "first", "second"]

    print groupAnagrams(input)

