class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None
        self.maxSum = None
        self.targetNode = None

    def findTargetLeaf(self, root, curSum):
        if root is None:
            return

        curSum += root.data

        if root.left is None and root.right is None:
            if curSum > self.maxSum:
                self.maxSum = curSum
                self.targetNode = root
            return

        self.findTargetLeaf(root.left, curSum)
        self.findTargetLeaf(root.right, curSum)


    def printPathToTargetLeaf(self, root):
        if root is None:
            return False

        if root == self.targetNode or self.printPathToTargetLeaf(root.left) or self.printPathToTargetLeaf(root.right):
            print root.data
            return True

        return False


if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(10)
    tree.root.left = Node(-2)
    tree.root.right = Node(7)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(-4)

    tree.findTargetLeaf(tree.root, 0)
    tree.printPathToTargetLeaf(tree.root)
    print tree.maxSum
