class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.current = self.head
        else:
            newNode = Node(value)
            self.current.next = newNode
            self.current = newNode

    def printList(self):
        node = self.head
        while node:
            print node.value,
            node = node.next

    def reverseKGroups(self, headNode, k):
        prev = None
        # next = None
        current = headNode
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next:
            headNode.next = self.reverseKGroups(next, k)

        return prev


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    # llist.push(6)

    llist.printList()
    print "\n\n"

    llist.head = llist.reverseKGroups(llist.head, 3)

    llist.printList()
