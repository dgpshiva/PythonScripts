# Create a list of Linked Lists using nodes at each level of a tree
# Eg:       1
#          /  \
#         2    3
# Output: [1, 2->3]

# Solution:
# Idea is to traverse the tree like BFS in a graph
# Create a list to hold the Linked Lists:   lll = []
# Create a queue. Put the root node in the queue:  queue = [1]
# Enter "EndOfLevel" in the queue:    queue = [1 "EndOfLevel"]
# Create a new Linked List:     ll = LinkedList()
# Pop from the queue till "EndOfLevel" reached
# Insert the poped node to the Linked List:   ll = [1]
# Insert its left and right child to the LinkedList ONLY IF they exist:     queue = ["EndOfLevel", 2, 3]
# When "EndOfLevel" reached, add the Linked List to the list of Linked Lists:   
# lll = [[1]]
# ONLY IF there are more elements, in the queue, add "EndOfLevel" to the queue and create a new LinkedList
# queue = [2, 3, "EndOfLevel"]
# ll = LinkedList()
# Continue till queue is empty


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





