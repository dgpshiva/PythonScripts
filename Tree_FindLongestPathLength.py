# Google interview 

# Given a binary tree, find max depth of the tree
# Write function that returns the length of longest path inside the tree
# Eg: 
#       1
#      /  \
#      2    3
#     / \
#     4  5
#    /    \
#    6      7
# 
# Ans: Longest path is through 6-4-2-5-7 = 6

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
class BTree:
    def __init__(self):
        self.root = None
    
    def returnMaxDepthUtil(self, node, depth):
        if node:
            depth += 1
            return max(self.returnMaxDepthUtil(node.left, depth), self.returnMaxDepthUtil(node.right, depth))
        
        return depth

    def returnMaxDepth(self, node):
        return self.returnMaxDepthUtil(node, 0)

    
    def returnMaxPathLength(self, node):
        if node:
            maxLeftDepth = self.returnMaxDepth(node.left)
            maxRightDepth = self.returnMaxDepth(node.right)
            maxPathLeft = self.returnMaxPathLength(node.left)
            maxPathRight = self.returnMaxPathLength(node.right)
            pathThruRootLength = maxLeftDepth + maxRightDepth + 1
            return max(pathThruRootLength, maxPathLeft, maxPathRight)
        return 0
        

if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(6)
    # tree.root.left.right.right = Node(7)
    

    # print tree.returnMaxDepthUtil(tree.root)
    print tree.returnMaxPathLength(tree.root)
