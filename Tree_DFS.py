class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def DFSUtil(self, node, value):
        if node:
            self.DFSUtil(node.left, value)
            if node.data == value:
                print node.data
            self.DFSUtil(node.right, value)

    def DFS(self, value):
        self.DFSUtil(self.root, value)


if __name__ == '__main__':
    tree = BTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    # tree.DFS(4)
    tree.DFS(9)
