# Indeed interview

# Create, insert and retrieve given an index from an unrolled linked list
# Unrolled linked list is a linked list where every node has an array for some length

# Eg: Node  -   Node    -   Node
#       
#       |          |           |

#       0          5          10
#       1          6          11
#       2          7          12
#       3          8          13
#       4          9          14

# Given index retrieve element from the unrolled linked list
# Eg: Index = 12 => Value = 12


class Node:
    def __init__(self):
        self.arr = [None] * 5
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        
    def insert(self, val):
        if self.tail.arr.count(None) > 0:
            i = 0
            while self.tail.arr[i] is not None:
                i += 1
            self.tail.arr[i] = val
        
        else:
            newNode = Node()
            self.tail.next = newNode
            self.tail = newNode
            self.tail.arr[0] = val

    def display(self):
        node = self.head
        while node:
            for element in node.arr:
                print str(element) + " ",
            node = node.next
    
    def returnElement(self, index):
        node = self.head
        i = 0
        while node is not None and i < index//5:
            node = node.next
            i += 1
        return node.arr[index%5] if node is not None else None


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    ll.display()
    print ""
    print ll.returnElement(6)
    print ll.returnElement(0)
    print ll.returnElement(2)
    print ll.returnElement(5)
    print ll.returnElement(7)
    print ll.returnElement(12)

