class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.maxSum = 0

    # Function to get max sum path from a node to its leaf
    def getMaxSumNodeToLeaf(self, node, curSum):
        if node:
            curSum += node.val
            if node.left is None and node.right is None:
                if curSum > self.maxSum:
                    self.maxSum = curSum
            self.getMaxSumNodeToLeaf(node.left, curSum)
            self.getMaxSumNodeToLeaf(node.right, curSum)
        return self.maxSum

    def returnMaxSum(self, node):
        if node:
            # For every node, get these 4 values:
            # Max sum path from node's left child to its leaf
            # Max sum path from node's right child to its leaf
            # Max sum path contained within left side 
            # Max sum path contained within right side 
            self.maxSum = 0
            leftMaxSumNodeToLeaf = self.getMaxSumNodeToLeaf(node.left, 0)
            self.maxSum = 0
            rightMaxSumNodeToLeaf = self.getMaxSumNodeToLeaf(node.right, 0)
            leftMaxSumLeafToLeaf = self.returnMaxSum(node.left)
            rightMaxSumLeafToLeaf = self.returnMaxSum(node.right)

            # Result will be max between these
            return max(leftMaxSumNodeToLeaf + rightMaxSumNodeToLeaf + node.val, leftMaxSumLeafToLeaf, rightMaxSumLeafToLeaf)


if __name__ == '__main__':
    t = Tree()
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.left.left = Node(4)
    t.root.left.right = Node(3)
    t.root.left.right.right = Node(4)
    t.root.right = Node(1)

    print t.returnMaxSum(t.root)

