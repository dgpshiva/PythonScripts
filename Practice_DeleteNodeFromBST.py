class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val


class Tree:
    def __init__(self):
        self.root = None
    
    def inOrder(self, node):
        if node:
            print str(node.val) + " ",
            self.inOrder(node.left)
            self.inOrder(node.right)

    
    def deleteNode(self, node, val):
        if not node:
            return 
        
        if val > node.val:
            node.right = self.deleteNode(node.right, val)
        elif val < node.val:
            node.left = self.deleteNode(node.left, val)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            else:
                parent = node.right
                child = node.right
                while child.left is not None:
                    parent = child
                    child = child.left
                node.val = child.val
                parent.left = child.right
        return node

        
if __name__ == '__main__':
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(8)
    tree.root.left.left = Node(7)
    tree.root.right = Node(14)
    tree.root.right.left = Node(13)
    tree.root.right.right = Node(16)
    tree.root.right.right.left = Node(15)
    tree.root.right.right.right = Node(17)

    tree.inOrder(tree.root)
    tree.deleteNode(tree.root, 14)
    print ""
    tree.inOrder(tree.root)
    tree.deleteNode(tree.root, 8)
    print ""
    tree.inOrder(tree.root)
    tree.deleteNode(tree.root, 16)
    print ""
    tree.inOrder(tree.root)

