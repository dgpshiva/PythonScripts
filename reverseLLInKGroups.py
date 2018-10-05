class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        node = self.head
        while node:
            print node.data,
            node = node.next

    def reverseInKGroups(self, head, k):
        prev = None
        current = head
        next = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverseInKGroups(next, k)

        return prev



if __name__ == '__main__':
    llist = LinkedList()
    # llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    llist.printList()

    llist.head = llist.reverseInKGroups(llist.head, 3)

    print "\n\n"

    llist.printList()
