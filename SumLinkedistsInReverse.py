class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def push(self, data):
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

    def printListInReverse(self, node):
        if node is None:
            return
        self.printListInReverse(node.next)
        print node.data,

def getListLength(llist):
    node = llist.head
    count = 0
    while node:
        count += 1
        node = node.next
    return count

carry = 0
result = LinkedList()
def addSameSize(firstNode, secondNode):
    global carry
    if firstNode is None:
        return

    addSameSize(firstNode.next, secondNode.next)

    sum = firstNode.data + secondNode.data + carry
    result.push(sum%10)
    carry = sum/10

def propagateCarry(node, cur):
    global carry
    if node != cur:
        propagateCarry(node.next, cur)
    sum = node.data + carry
    result.push(sum%10)
    carry = sum/10


def sumListsInReverse(first, second):
    length1 = getListLength(first)
    length2 = getListLength(second)

    if length1 == length2:
        addSameSize(first.head, second.head)
    elif length1 > length2:
        diff = length1 - length2
        node1 = first.head
        node2 = second.head
        for i in range(0, diff):
            temp = node1
            node1 = node1.next
        addSameSize(node1, node2)
        propagateCarry(first.head, temp)
    elif length2 > length1:
        diff = length2 - length1
        node1 = first.head
        node2 = second.head
        for i in range(0, diff):
            temp = node2
            node2 = node2.next
        addSameSize(node1, node2)
        propagateCarry(second.head, temp)

    if carry > 0:
        result.push(carry)


if __name__ == '__main__':
    first = LinkedList()
    first.push(5)
    first.push(6)
    first.push(3)
    # first.push(2)
    # first.push(9)
    first.printList()
    print "\n\n"

    second = LinkedList()
    second.push(8)
    second.push(4)
    second.push(2)
    second.push(9)
    second.push(9)
    second.printList()
    print "\n\n"

    print getListLength(first)
    print getListLength(second)
    print "\n\n"

    sumListsInReverse(first, second)

    result.printListInReverse(result.head)







