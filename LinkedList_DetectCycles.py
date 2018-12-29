class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def detectCycle(self):
        if self.head is None or self.head.next is None:
            return False

        slow = self.head
        fast = self.head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(3)

    node = Node(2)
    ll.head.next = node

    ll.head.next.next = Node(0)
    ll.head.next.next.next = Node(-4)
    ll.head.next.next.next.next = node

    print ll.detectCycle()


