class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def checkIfBST(self, node, min, max):
        if node is None:
            return True

        if (min != None and node.data <= min) or (max != None and node.data > max):
            return False

        if (not self.checkIfBST(node.left, min, node.data) or not self.checkIfBST(node.right, node.data, min)):
            return False

        return True


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(16)
    tree.root.left = Node(10)
    tree.root.right = Node(30)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(15)
    tree.root.left.left.left = Node(7)
    tree.root.left.left.right = Node(9)

    print tree.checkIfBST(tree.root, None, None)

