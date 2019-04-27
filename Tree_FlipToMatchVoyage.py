# Given a voyage (array of integers), flip required nodes of tree so that its pre order traversal equals the voyage
# Flipping a node means making left node as right and vice versa
# Eg:       1
#          /  \
#         2    3
# voyage = [1, 3, 2]
# output = [1]

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

        # At every node, check if its value equals voyage[i]
        if root.val != voyage[self.i]:
           return False

        # If yes, increment i by 1 and go the next element in the voyage
        self.i += 1
        # If the left node exists and its value does not equal voyage[i], make a flip
        if root.left and root.left.val != voyage[self.i]:
            output.append(root.val)
            root.left, root.right = root.right, root.left

        # Proceed to all the remaining nodes of the tree
        return self.preOrder(root.left, voyage, output) and self.preOrder(root.right, voyage, output)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    voyage = [1, 3, 2]
    print s.flipMatchVoyage(root, voyage)
