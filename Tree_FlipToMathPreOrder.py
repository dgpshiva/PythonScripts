class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.i = 0

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        output = []
        return output if self.preOrder(root, voyage, output) else [-1]

    def preOrder(self, root, voyage, output):
        if not root:
            return True

        if root.val != voyage[self.i]:
           return False

        self.i += 1
        if root.left and root.left.val != voyage[self.i]:
            output.append(root.val)
            root.left, root.right = root.right, root.left

        return self.preOrder(root.left, voyage, output) and self.preOrder(root.right, voyage, output)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    voyage = [1, 3, 2]
    print s.flipMatchVoyage(root, voyage)
