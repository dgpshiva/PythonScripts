class StoreSearchDescriptions:
    def __init__(self):
        self.indexWords = {}

    def storeDescription(self, description, document_number):
        self.indexWords[document_number] = set(description.split(" "))

    def searchDescriptions(self, search):
        indexMatchCounts = []
        words = search.split(" ")
        for index in self.indexWords:
            count = 0
            for word in words:
                if word in self.indexWords[index]:
                    count += 1
            indexMatchCounts.append((index, count))

        indexMatchCounts = sorted(indexMatchCounts, key=lambda element: (-element[1], element[0]))
        print indexMatchCounts

        strOutput = ""
        i = 0
        for indexMatchCount in indexMatchCounts:
            if indexMatchCount[1] > 0:
                strOutput += str(indexMatchCount[0]) + " "
                i += 1
                if i == 10:
                    break

        print strOutput


if __name__ == '__main__':
    s = StoreSearchDescriptions()
    descriptions = ["software engineer", "software javascript", "engineer javascript"]
    M = 3
    searches = ["software", "engineer javascript", "software engineer"]
    N = 1

    for document_number in range(M):
        s.storeDescription(descriptions[document_number], document_number)

    for search in searches:
        s.searchDescriptions(search)

