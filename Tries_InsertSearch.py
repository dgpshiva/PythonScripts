import unittest

class TestsClass(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        keys = ["key", "test", 'shiva', "nivi"]
        for key in keys:
            self.trie.insert(key)

    def testOutput(self):
        op = self.trie.search("temp")
        self.assertTrue(op)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToindex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToindex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.endOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToindex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl and pCrawl.endOfWord


if __name__ == '__main__':
    unittest.main()

