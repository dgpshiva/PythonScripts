class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = LinkedListNode(data)
            node.next = newNode


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.LinkedListsList = []

    def createLinkedLists(self):
        linkedList = LinkedList()
        queue = []
        node = self.root
        if node:
            queue.append(node)
            queue.append(Node("EndOfLevel"))
        while queue:
            node = queue.pop(0)
            if node.data != "EndOfLevel":
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                linkedList.insert(node.data)
            else:
                self.LinkedListsList.append(linkedList)
                if queue:
                    linkedList = LinkedList()
                    queue.append(Node("EndOfLevel"))


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    tree.createLinkedLists()

    for linkedList in tree.LinkedListsList:
        node = linkedList.head
        while node:
            print str(node.data) + " ",
            node = node.next
        print ""





