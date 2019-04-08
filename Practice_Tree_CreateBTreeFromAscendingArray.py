class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BTree:
    def __init__(self):
        self.root = None
    
    def createBTree(self, arr):
        if len(arr) < 1:
            return None
        
        mid = (len(arr)-1)//2
        node = Node(arr[mid])
        node.left = self.createBTree(arr[0:mid])
        node.right = self.createBTree(arr[mid+1:len(arr)])
        return node
    
    def preOrder(self, node):
        if node:
            print str(node.value) + " ",
            self.preOrder(node.left)
            self.preOrder(node.right)


if __name__ == "__main__":
    b = BTree()
    # b.root = b.createBTree([10, 20, 30])
    b.root = b.createBTree([10, 20, 30, 40, 50, 60, 70])
    b.preOrder(b.root)
