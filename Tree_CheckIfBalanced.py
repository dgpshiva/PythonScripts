# Check if tree is balanced.
# Balanced tree is one where height of two sub trees of any node never differ by more than one.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.isBalanced = None
        self.lheight = self.rheight = None

class Tree:
    def __init__(self):
        self.root = None

    def display(self, node):
        if node:
            print node.val
            self.display(node.left)
            self.display(node.right)

    def returnHeight(self, node):
        if node:
            node.lheight = self.returnHeight(node.left)
            node.rheight = self.returnHeight(node.right)
            node.isBalanced = True if abs(node.lheight - node.rheight) <=1 else False
            return max(node.lheight, node.rheight) + 1
        return 0


if __name__ == '__main__':
    tree = Tree()

    tree.root = Node(5)
    tree.root.left = Node(4)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(6)

    tree.root.right = Node(10)
    tree.root.right.left = Node(9)
    tree.root.right.right = Node(11)
    tree.root.right.right.right = Node(12)
    # tree.root.right.right.right.right = Node(13)

    # tree.display(tree.root)
    
    tree.returnHeight(tree.root)
    print tree.root.isBalanced