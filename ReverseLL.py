class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def printList(self):
        node = self.head
        while (node):
            print node.data
            node = node.next

    def reverse(self):
        prev = None
        current = self.head

        while (current):
            next = current.next
            current.next = prev

            prev = current
            current = next

        self.head = prev


if __name__ == '__main__':
    llist = LinkedList()

    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)

    llist.reverse()

    llist.printList()
