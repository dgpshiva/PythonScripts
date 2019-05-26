class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val

class Tree:
    def __init__(self):
        self.root = None
    
    def checkIfBST(self, node, min, max):
        if node is None:
            return True
        
        if (min is not None and node.val <= min) or (max is not None and node.val > max):
            return False
        
        return self.checkIfBST(node.left, min, node.val) and self.checkIfBST(node.right, node.val, max)
    

if __name__ == '__main__':
    tree = Tree()
    # tree.root = Node(16)
    # tree.root.left = Node(10)
    # tree.root.right = Node(30)
    # tree.root.left.left = Node(8)
    # tree.root.left.right = Node(15)
    # tree.root.left.left.left = Node(7)
    # tree.root.left.left.right = Node(9)

    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(1)
    tree.root.right = Node(8)
    tree.root.right.left = Node(7)
    tree.root.right.right = Node(9)

    print tree.checkIfBST(tree.root, None, None)