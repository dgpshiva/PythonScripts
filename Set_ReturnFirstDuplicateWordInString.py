def returnFirstDuplicateWord(input):
    s = set()

    words = input.split(' ')

    for word in words:
        if word != ' ':
            if word.lower() in s:
                return word
            else:
                s.add(word.lower())

if __name__ == '__main__':
    input = "This is a test. this is is a test"
    print returnFirstDuplicateWord(input)
