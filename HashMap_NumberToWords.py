class NumberToWords:
    def __init__(self):
        self.unitsDigits = {1:"one", 2:'two', 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
        self.teensDigits = {1:"eleven", 2:'twelve', 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}
        self.tensDigits = {2:'twenty', 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

    def returnWordsForNumber(self, number):
        output = ""
        lastIndex = len(number) - 1
        for i in range(0, len(number)):
            if lastIndex - i == 3 and int(number[i]) in self.unitsDigits:
                output += self.unitsDigits[int(number[i])] + " thousand "
            elif lastIndex - i == 2 and int(number[i]) in self.unitsDigits:
                output += self.unitsDigits[int(number[i])] + " hundred "
            elif lastIndex - i == 1:
                if int(number[i]) == 0 and int(number[i]) in self.unitsDigits:
                    output += self.unitsDigits[int(number[i+1])]
                    return output
                if int(number[i]) == 1 and int(number[i]) in self.teensDigits:
                    output += self.teensDigits[int(number[i+1])]
                    return output
                else:
                    if int(number[i]) in self.tensDigits:
                        output += self.tensDigits[int(number[i])] + " "
                    if int(number[i+1]) in self.unitsDigits:
                        output += self.unitsDigits[int(number[i+1])]
                    return output
            elif lastIndex - i == 0 and int(number[i]) in self.unitsDigits:
                output += self.unitsDigits[int(number[i])]
                return output


if __name__ == '__main__':
    n = NumberToWords()
    # print n.returnWordsForNumber("1234")
    # print n.returnWordsForNumber("9923")
    # print n.returnWordsForNumber("523")
    # print n.returnWordsForNumber("89")
    # print n.returnWordsForNumber("8989")
    # print n.returnWordsForNumber("1214")
    # print n.returnWordsForNumber("513")
    # print n.returnWordsForNumber("13")
    # print n.returnWordsForNumber("3")
    # print n.returnWordsForNumber("1200")
    # print n.returnWordsForNumber("1204")
    # print n.returnWordsForNumber("1240")
    # print n.returnWordsForNumber("1040")
    # print n.returnWordsForNumber("0040")
    # print n.returnWordsForNumber("0004")
    # print n.returnWordsForNumber("0000")
    print n.returnWordsForNumber("11234")



