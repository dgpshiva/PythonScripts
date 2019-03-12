class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def mergeLists(l1, l2):
    preHead = Node(-1)

    prev = preHead
    while l1 and l2:
        if l1.data <= l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return preHead.next


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.head = Node(1)
    ll1.head.next = Node(2)
    ll1.head.next.next = Node(4)

    ll2 = LinkedList()
    ll2.head = Node(1)
    ll2.head.next = Node(3)
    ll2.head.next.next = Node(4)

    node = mergeLists(ll1.head, ll2.head)

    while node:
        print str(node.data) + " ",
        node = node.next

