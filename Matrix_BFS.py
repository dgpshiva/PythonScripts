def findPath(grid, rows, cols):
    queue = []

    visited = [[0 for x in range(0, rows)] for y in range(0, cols)]

    start = (0, 0, 0)
    queue.append(start)
    visited[0][0] = 1

    while queue:
        current = queue.pop()
        if grid[current[0]][current[1]] == 9:
            return current[2]
        else:
            if current[0]-1 >= 0 and visited[current[0]-1][current[1]] != 1 and grid[current[0]-1][current[1]] != 1:
                queue.insert(0, (current[0]-1, current[1], current[2]+1))
                visited[current[0]-1][current[1]] = 1
            if current[1]-1 >= 0 and visited[current[0]][current[1]-1] != 1 and grid[current[0]][current[1]-1] != 1:
                queue.insert(0, (current[0], current[1]-1, current[2]+1))
                visited[current[0]][current[1]-1] = 1
            if current[0]+1 < rows and visited[current[0]+1][current[1]] != 1 and grid[current[0]+1][current[1]] != 1:
                queue.insert(0, (current[0]+1, current[1], current[2]+1))
                visited[current[0]+1][current[1]] = 1
            if current[1]+1 < cols and visited[current[0]][current[1]+1] != 1 and grid[current[0]][current[1]+1] != 1:
                queue.insert(0, (current[0], current[1]+1, current[2]+1))
                visited[current[0]][current[1]+1] = 1

    return -1


if __name__ == '__main__':
    grid = [[0, 1, 0], [0, 0, 1], [0, 9, 1]]
    print findPath(grid, 3, 3)
    #grid = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 9, 1], [0, 0, 0, 0]]
    # print findPath(grid, 4, 4)
