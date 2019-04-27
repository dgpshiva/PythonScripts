class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
class Tree:
    def __init__(self, voyage):
        self.root = None
        self.i = 0
        self.voyage = voyage
        self.output = []
    
    def flipMatchVoyage(self):
        return self.output if self.preOrder(self.root) else -1
    
    def preOrder(self, node):
        if node is None:
            return True
        
        if node.val != self.voyage[self.i]:
            return False
        
        self.i += 1
        if node.left and node.left.val != self.voyage[self.i]:
            self.output.append(node.val)
            node.left, node.right = node.right, node.left
        
        return self.preOrder(node.left) and self.preOrder(node.right)


if __name__ == '__main__':
    voyage = [1, 3, 2]
    t = Tree(voyage)
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.right = Node(3)

    print t.flipMatchVoyage()