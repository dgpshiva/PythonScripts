class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
    

class Tree:
    def __init__(self):
        self.root = None
    
    def findLCABinarySearchTree(self, node, n1, n2):
        if node is None:
            return None
        
        if node.value > n1 and node.value > n2:
            return self.findLCABinarySearchTree(node.left, n1, n2)
        elif node.value < n1 and node.value < n2:
            return self.findLCABinarySearchTree(node.right, n1, n2)
        
        return node
    
    def findLCABinaryTree(self, node, n1, n2):
        if not node:
            return None
        
        if node.value == n1 or node.value == n2:
            return node
        
        leftLCA = self.findLCABinaryTree(node.left, n1, n2)
        rightLCA = self.findLCABinaryTree(node.right, n1, n2)

        if leftLCA and rightLCA:
            return node
        
        return leftLCA if leftLCA is not None else rightLCA


if __name__ == '__main__':
    t = Tree()
    t.root = Node(20)
    t.root.left = Node(8)
    t.root.right = Node(22)
    t.root.left.left = Node(4)
    t.root.left.right = Node(12)
    t.root.left.right.left = Node(10)
    t.root.left.right.right = Node(14)
    # print t.findLCABinarySearchTree(t.root, 10, 14).value
    # print t.findLCABinarySearchTree(t.root, 14, 8).value
    # print t.findLCABinarySearchTree(t.root, 10, 22).value

    t.root = Node(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.left = Node(4)
    t.root.left.right = Node(5)
    t.root.right.left = Node(6)
    t.root.right.right = Node(7)
    print t.findLCABinaryTree(t.root, 4, 5).value
    print t.findLCABinaryTree(t.root, 4, 6).value
    print t.findLCABinaryTree(t.root, 3, 4).value
    print t.findLCABinaryTree(t.root, 2, 4).value

