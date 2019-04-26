# Insert words into Trie datastructure and 
# then search if a word exists

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
     # Every Trie node can have upto 26 children (for chars a to z)
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
            # Eg: For "key", 10th child of root will have a Trie Node, all others will be None (ascii value of k = 107 and a = 97, so 107 - 97 = 10)
            # Then the 4th child of above node will have a Trie Node, all others will be None and so on (ascii value of e = 101 and a = 97, so 101 - 97 = 4)
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
