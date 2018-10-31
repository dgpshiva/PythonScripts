class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BTree:
    def __init__(self):
        self.root = None
        self.maxSum = None

    def findMaxSumPath(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            return root.data

        ls = self.findMaxSumPath(root.left)
        rs = self.findMaxSumPath(root.right)

        if root.left is not None and root.right is not None:
            self.maxSum = max(self.maxSum, ls + rs + root.data)
            return max(ls, rs) + root.data

        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data


if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(-15)
    tree.root.left = Node(5)
    tree.root.right = Node(6)
    tree.root.left.left = Node(-8)
    tree.root.left.right = Node(1)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.right = Node(6)
    tree.root.right.left = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.right.right= Node(0)
    tree.root.right.right.right.left = Node(4)
    tree.root.right.right.right.right = Node(-1)
    tree.root.right.right.right.right.left = Node(10)

    # tree.root = Node(10)
    # tree.root.right = Node(2)
    # tree.root.left = Node(8)
    # tree.root.left.left = Node(3)
    # tree.root.left.right = Node(5)

    tree.findMaxSumPath(tree.root)
    print tree.maxSum