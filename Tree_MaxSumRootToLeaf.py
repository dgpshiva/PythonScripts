# Find the max sum inside binary tree from root to leaf
# and print the path from that leaf to the root

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None
        self.maxSum = None  # variable to store the max sum value
        self.targetNode = None  # variable to hold the target leaf node to which sum is max from root


    def findTargetLeafNode(self, node, curSum):
        if node:
            # For every node keep summing the node values
            curSum += node.data

            # If the node is a leaf
            if node.left is None and node.right is None:
                # Check if this is the target leaf node
                if curSum > self.maxSum:
                    self.maxSum = curSum
                    self.targetNode = node  # Store this target leaf node

            self.findTargetLeafNode(node.left, curSum)
            self.findTargetLeafNode(node.right, curSum)


    def printPathToTargetLeaf(self, node):
        if node is None:
            return False

        # Whenever we find our target leaf node, this becomes True and we print the node value.
        # And from there we keep returning True, so path from this target node to root gets printed
        if node == self.targetNode or self.printPathToTargetLeaf(node.left) or self.printPathToTargetLeaf(node.right):
            print node.data
            return True



if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(10)
    tree.root.left = Node(-2)
    tree.root.right = Node(7)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(-4)

    tree.findTargetLeafNode(tree.root, 0)
    tree.printPathToTargetLeaf(tree.root)
    print tree.maxSum

    print ""
    tree.root = Node(10)
    tree.root.left = Node(7)
    tree.root.right = Node(-2)
    tree.root.left.left = Node(-4)
    tree.root.left.right = Node(8)

    tree.findTargetLeafNode(tree.root, 0)
    tree.printPathToTargetLeaf(tree.root)
    print tree.maxSum
