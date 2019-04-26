class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        self.maxSum = 0
        self.targetNode = None
    
    def maxSumRootToLeaf(self, node, curSum):
        if node:
            curSum += node.val
            if node.left is None and node.right is None:
                if curSum > self.maxSum:
                    self.maxSum = curSum
                    self.targetNode = node
            
            self.maxSumRootToLeaf(node.left, curSum)
            self.maxSumRootToLeaf(node.right, curSum)

    def pathToTargetLeaf(self, node):
        if node is None:
            return False

        if node == self.targetNode or self.pathToTargetLeaf(node.left) or self.pathToTargetLeaf(node.right):
            print node.val
            return True


if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(7)
    tree.root.right = Node(-2)
    tree.root.left.left = Node(-4)
    tree.root.left.right = Node(8)

    tree.maxSumRootToLeaf(tree.root, 0)
    tree.pathToTargetLeaf(tree.root)
    print tree.maxSum