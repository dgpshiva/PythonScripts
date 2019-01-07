class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        output = []
        self.preOrder(root, voyage, 0, output)
        return output


    def preOrder(self, root, voyage, i, output):
        if root:
            if root.val == voyage[i]:
                if not self.preOrder(root.left, voyage, i+1, output) or self.preOrder(root.right, voyage, i+2, output):
                    output.append(root.val)
                    temp = root.left
                    root.left = root.right
                    root.right = temp
            else:
                return False

        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    voyage = [1, 2, 3]
    print s.flipMatchVoyage(root, voyage)

