def countWordsFreq(input):
    wordCount = {}
    words = input.split(' ')
    for word in words:
        if word.lower() in wordCount:
            wordCount[word.lower()] += 1
        else:
            wordCount[word.lower()] = 1

    return wordCount


if __name__ == '__main__':
    input = "This is a test and lets hope that this works. The name is the Nivi and Shiva!"
    print countWordsFreq(input)
