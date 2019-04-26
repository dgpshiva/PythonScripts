import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        keys = ["this", "and", "that"]
        for key in keys:
            self.t.insert(key)

    def testSearch(self):
        self.assertTrue(self.t.search("test"))
            

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endofword = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def getIndex(self, val):
        return ord(val) - ord('a')
    
    def insert(self, key):
        pCrawl = self.root
        for k in key:
            index = self.getIndex(k)
            if pCrawl.children[index] is None:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.endofword = True

    def search(self, key):
        pCrawl = self.root
        for k in key:
            index = self.getIndex(k)
            if pCrawl.children[index] is None:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.endofword


if __name__ == '__main__':
    unittest.main()
    # t = Trie()
    # t.insert("key")
    # t.insert("some")
    # t.insert("thing")

    # print t.search("key")
    # print t.search("test")