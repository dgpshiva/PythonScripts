def DFSUtil(input, visited, currentCell, rows, cols, value):
    visited[currentCell[0]][currentCell[1]] = 1
    if input[currentCell[0]][currentCell[1]] == value:
        return currentCell
    else:
        if currentCell[0]-1>=0 and visited[currentCell[0]-1][currentCell[1]] != 1:
            nextCell = (currentCell[0]-1, currentCell[1])
            return DFSUtil(input, visited, nextCell, rows, cols, value)
        if currentCell[1]-1>=0 and visited[currentCell[0]][currentCell[1]-1] != 1:
            nextCell = (currentCell[0], currentCell[1]-1)
            return DFSUtil(input, visited, nextCell, rows, cols, value)
        if currentCell[0]+1<rows and visited[currentCell[0]+1][currentCell[1]] != 1:
            nextCell = (currentCell[0]+1, currentCell[1])
            return DFSUtil(input, visited, nextCell, rows, cols, value)
        if currentCell[1]+1<cols and visited[currentCell[0]][currentCell[1]+1] != 1:
            nextCell = (currentCell[0], currentCell[1]+1)
            return DFSUtil(input, visited, nextCell, rows, cols, value)

    return -1


def DFS(input, rows, cols, value):
    visited = [[0 for x in range(0, rows)] for y in range(0, cols)]

    startCell = (0, 0)
    return DFSUtil(input, visited, startCell, rows, cols, value)


if __name__ == '__main__':
    grid = [[0, 1, 0], [0, 9, 1], [0, 0, 1]]
    print DFS(grid, 3, 3, 9)
    # print DFS(grid, 3, 3, -9)
