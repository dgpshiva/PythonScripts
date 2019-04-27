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


from collections import deque

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    
    def insert(self, val):
        if self.head is None:
            self.head = self.tail = LinkedListNode(val)
        else:
            node = LinkedListNode(val)
            self.tail.next = node
            self.tail = node
    
    def display(self):
        node = self.head
        while node:
            print str(node.val) + " ",
            node = node.next


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    def createLinkedLists(self):
        lll = []
        if self.root is None:
            return lll
        queue = deque()
        queue.append(self.root)
        queue.append("EndOfLevel")
        ll = LinkedList()
        while queue:
            q = queue.popleft()
            if q != "EndOfLevel":
                ll.insert(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            else:
                lll.append(ll)
                if queue:
                    queue.append("EndOfLevel")
                    ll = LinkedList()
        
        return lll


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    lll = tree.createLinkedLists()

    for linkedList in lll:
        node = linkedList.head
        while node:
            print str(node.val) + " ",
            node = node.next
        print ""


