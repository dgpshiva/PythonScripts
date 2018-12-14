class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def create(self, input, first, last, node):
        if first == last:
            leafNode = Node(input[first])
            return leafNode
        mid = (first+last)//2
        node.data = input[mid]
        node.left = self.create(input, first, mid-1, Node(None))
        node.right = self.create(input, mid+1, last, Node(None))

        return node

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print str(node.data) + " ",
            self.inOrder(node.right)


if __name__ == '__main__':
    input = [1, 3, 6, 10, 15, 17, 20]
    tree = BSTree()
    tree.root = Node(None)
    tree.root = tree.create(input, 0, len(input)-1, tree.root)

    tree.inOrder(tree.root)
