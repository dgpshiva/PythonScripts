class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushInReverse(self, data):
        if self.head is None:
            self.head = Node(data)
            self.current = self.head
        else:
            newNode = Node(data)
            self.current.next = newNode
            self.current = newNode

    def printList(self):
        node = self.head
        while node:
            print node.data,
            node = node.next


def sumLinkedLists(list1, list2):
    outputList = LinkedList()

    node1 = list1.head
    node2 = list2.head
    q = 0

    while node1 and node2:
        temp = (node1.data + node2.data + q)/10
        r = (node1.data + node2.data + q)%10
        outputList.pushInReverse(r)
        q = temp
        node1 = node1.next
        node2 = node2.next

    if node1 is not None:
        while node1:
            temp = (node1.data + q)/10
            r = (node1.data + q)%10
            outputList.pushInReverse(r)
            q = temp
            node1 = node1.next
    elif node2 is not None:
        while node2:
            temp = (node2.data + q)/10
            r = (node2.data + q)%10
            outputList.pushInReverse(r)
            q = temp
            node2 = node2.next

    return outputList


if __name__ == '__main__':
    first = LinkedList()
    first.push(6)
    first.push(4)
    first.push(9)
    first.push(5)
    first.push(7)

    first.printList()
    print "\n\n"

    second = LinkedList()
    second.push(4)
    second.push(8)
    second.printList()
    print "\n\n"

    output = sumLinkedLists(first, second)
    output.printList()
