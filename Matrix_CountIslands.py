class Graph:
    def __init__(self, rows, cols, g):
        self.graph = g
        self.rows = rows
        self.cols = cols

    def isSafe(self, i, j, visited):
        return i>=0 and j >=0 and i<self.rows and j<self.cols and not visited[i][j] and self.graph[i][j]

    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        visited[i][j] = True

        for k in range(8):
            if self.isSafe(i+rowNbr[k], j+colNbr[k], visited):
                self.DFS(i+rowNbr[k], j+colNbr[k], visited)

    def countIslands(self):
        visited = [[False for i in range(self.rows)] for j in range(self.cols)]
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if not visited[i][j] and self.graph[i][j] == 1:
                    count += 1
                    self.DFS(i, j, visited)


        return count

