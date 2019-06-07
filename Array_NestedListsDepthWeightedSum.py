# Find the depth weighted sum of a nested list
# Eg: [[1,1], 2, [1, 1]]
# Output: 10
# There are four 1s at level 2 and one 2 at level 1 = 4 * 2 + 2 * 1 = 10 

# Eg: [1, [4, [6]]]
# Output: 27
# 1 * 1 + 4 * 2 + 6 * 3 = 27

from collections import deque

class Solution:
    def isInteger(self, element):
        return isinstance(element, int)
    
    def getInteger(self, element):
        return int(element)
    
    def getList(self, element):
        return element

    # Recursive solution
    def depthSum(self, nestedList, depth):
        output = 0
        for element in nestedList:
            if self.isInteger(element):
                output += self.getInteger(element) * depth
            else:
                output += self.depthSum(self.getList(element), depth+1)
        
        return output

    # Breadth First Traversal solution
    def depthSumBFT(self, nestedList):
        elementQueue = deque()
        depthQueue = deque()

        for element in nestedList:
            elementQueue.append(element)
            depthQueue.append(1)
        
        output = 0
        while elementQueue:
            element = elementQueue.popleft()
            depth = depthQueue.popleft()

            if self.isInteger(element):
                output += self.getInteger(element) * depth
            else:
                for item in self.getList(element):
                    elementQueue.append(item)
                    depthQueue.append(depth+1)

        return output


if __name__ == '__main__':
    s = Solution()
    print s.depthSum([[1,1], 2, [1, 1]], 1)
    print s.depthSum([1, [4, [6]]], 1)

    print s.depthSumBFT([[1,1], 2, [1, 1]])
    print s.depthSumBFT([1, [4, [6]]])

