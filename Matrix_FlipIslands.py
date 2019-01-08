class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if rows > 0:
            cols = len(board[0])

            # visited = [[False for i in range(0, cols)] for j in range(0, rows)]

            # negPoints = []
            negPoints = [[False for i in range(0, cols)] for j in range(0, rows)]
            for i in range(0, cols):
                negPoints[0][i] = True
                negPoints[rows-1][i] = True
            for j in range(0, rows):
                negPoints[j][0] = True
                negPoints[j][cols-1] = True

            for i in range(1, rows-1):
                for j in range(1, cols-1):
                    if board[i][j] == 'O' and not negPoints[i][j]:
                        islandPoints = []
                        visited = [[False for k in range(0, cols)] for l in range(0, rows)]
                        valid = self.DFS(i, j, board, visited, rows, cols, islandPoints, negPoints)
                        if valid:
                            for point in islandPoints:
                                board[point[0]][point[1]] = 'X'
                        else:
                            for point in negPoints:
                                # negPoints.extend(islandPoints)
                                negPoints[point[0]][point[1]] = True
        return board

    def DFS(self, i, j, board, visited, rows, cols, islandPoints, negPoints):
        visited[i][j] = True
        islandPoints.append((i, j))
        adjRows = [-1, 0, 0, 1]
        adjCols = [0, -1, 1, 0]

        for k in range(0, len(adjRows)):
            if i+adjRows[k]<rows and j+adjCols[k]<cols:
                if board[i+adjRows[k]][j+adjCols[k]] == 'O' and ( i+adjRows[k]==0 or i+adjRows[k]==rows-1 or j+adjCols[k]==0 or j+adjCols[k]==cols-1 or negPoints[i+adjRows[k]][j+adjCols[k]]==True ):
                    return False
                elif board[i+adjRows[k]][j+adjCols[k]] == 'O' and not visited[i+adjRows[k]][j+adjCols[k]]:
                    valid = self.DFS(i+adjRows[k], j+adjCols[k], board, visited, rows, cols, islandPoints, negPoints)
                    if not valid:
                        return False
        return True


s = Solution()
# print s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# print s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])
# print s.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])
# print s.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
print s.solve([["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]])