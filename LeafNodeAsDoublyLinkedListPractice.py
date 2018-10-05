class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def extractLeafList(root):
    if root is None:
        return None

    if root.left is None and root.right is None:
        root.right = extractLeafList.head

        if extractLeafList.head is not None:
            extractLeafList.head.left = root

        extractLeafList.head = root

        return None

    root.right = extractLeafList(root.right)
    root.left = extractLeafList(root.left)

    return root


def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print root.data
        printInOrder(root.right)

def printList(head):
    while(head):
        if head.data is not None:
            print head.data
        head = head.right


if __name__ == '__main__':
    extractLeafList.head = Node(None)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    print "Tree before:\n"
    printInOrder(root)
    print "\n\n"

    root = extractLeafList(root)

    print "Tree after:\n"
    printInOrder(root)
    print "\n\n"

    print "List:\n"
    printList(extractLeafList.head)
    print "\n\n"



