import ctypes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, maxSize):
        self.head = None
        self.tail = None
        self.maxSize = maxSize
        self.currentSize = 1
        self.hash = {}

    def addToCache(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.hash[data] = id(self.head)
        elif self.currentSize < self.maxSize:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.currentSize += 1
            self.hash[data] = id(newNode)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.hash[data] = id(newNode)

            tailNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            tailNode.prev = None
            del self.hash[tailNode.data]
            del tailNode


    def updateCache(self, data):
        node = ctypes.cast(self.hash[data], ctypes.py_object).value
        if node != self.head:
            if node == self.tail:
                node.prev.next = node.next
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node



if __name__ == '__main__':
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

    cache = LRUCache(3)

    for page in pages:
        if page in cache.hash:
            node = ctypes.cast(cache.hash[page], ctypes.py_object).value
            print node.data
            cache.updateCache(page)
        else:
            cache.addToCache(page)
