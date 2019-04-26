class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BTree:
    def __init__(self):
        self.root = None
        self.maxSum = None

    def findMaxSum(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            return root.data

        ls = self.findMaxSum(root.left)
        rs = self.findMaxSum(root.right)

        if root.left is not None and root.right is not None:
            self.maxSum = max(self.maxSum, ls + rs + root.data)
            return max(ls, rs) + root.data

        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data


if __name__ == '__main__':
    tree = BTree()
    # tree.root = Node(-15)
    # tree.root.left = Node(5)
    # tree.root.right = Node(6)
    # tree.root.left.left = Node(-8)
    # tree.root.left.right = Node(1)
    # tree.root.left.left.left = Node(2)
    # tree.root.left.left.right = Node(6)
    # tree.root.right.left = Node(3)
    # tree.root.right.right = Node(9)
    # tree.root.right.right.right= Node(0)
    # tree.root.right.right.right.left = Node(4)
    # tree.root.right.right.right.right = Node(-1)
    # tree.root.right.right.right.right.left = Node(10)

    tree.root = Node(10)
    tree.root.right = Node(2)
    tree.root.left = Node(8)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(5)

    t = BTree()
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.left.left = Node(4)
    t.root.left.right = Node(3)
    t.root.left.right.right = Node(4)
    t.root.right = Node(1)

    t.findMaxSum(t.root)
    print t.maxSum
