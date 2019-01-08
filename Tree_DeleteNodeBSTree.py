class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            node = Node(data)
            return node
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            print str(node.data) + " ",
            self.inOrder(node.right)

    def deleteNode(self, node, data):
        if node is None:
            return
        elif data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                parent = node.right
                child = node.right
                while child.left is not None:
                    parent = child
                    child = child.left
                node.data = child.data
                parent.left = child.right
        return node


if __name__ == '__main__':
    tree = BTree()
    tree.root = tree.insert(tree.root, 50)
    tree.root = tree.insert(tree.root, 30)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 40)
    tree.root = tree.insert(tree.root, 70)
    tree.root = tree.insert(tree.root, 60)
    tree.root = tree.insert(tree.root, 80)

    tree.inOrder(tree.root)
    print ""

    tree.root = tree.deleteNode(tree.root, 20)

    tree.inOrder(tree.root)
    print ""

    tree.root = tree.deleteNode(tree.root, 30)

    tree.inOrder(tree.root)
    print ""

    tree.root = tree.deleteNode(tree.root, 50)

    tree.inOrder(tree.root)
    print ""

    print tree.root.data


