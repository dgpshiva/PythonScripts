class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def InOrder(self, node, output):
        if node is not None:
            self.InOrder(node.left, output)
            output.append(node.data)
            self.InOrder(node.right, output)

    def PreOrder(self, node):
        if node is not None:
            print node.data
            self.PreOrder(node.left)
            self.PreOrder(node.right)

    def PostOrder(self, node):
        if node is not None:
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print node.data


if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(9)
    tree.root.left = Node(7)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(8)
    tree.root.right = Node(11)
    tree.root.right.left = Node(10)
    tree.root.right.right = Node(12)

    output = []
    tree.InOrder(tree.root, output)
    # print output

    # tree.PreOrder(tree.root)

    tree.PostOrder(tree.root)
