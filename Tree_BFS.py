class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def BFS(self, value):
        if self.root == None:
            return None

        queue = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0)
            if node.data == value:
                return node.data
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return None


if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print tree.BFS(9)