def rotateMatrix(mat):
    N = len(mat)

    for layer in range(0, N/2):
        first = layer
        last = N - 1 - layer

        for i in range(first, last):
            offset = i - first

            top = mat[first][i]
            mat[first][i] = mat[last-offset][first]
            mat[last-offset][first] = mat[last][last-offset]
            mat[last][last-offset] = mat[i][last]
            mat[i][last] = top


def displayMatrix(mat):
    N = len(mat)
    for i in range(0, N):
        for j in range(0, N):
            print str(mat[i][j]) + " ",
        print "\n"


if __name__ == '__main__':
    mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]

    '''
    # Test case 2
    mat = [ [1, 2, 3 ],
            [4, 5, 6 ],
            [7, 8, 9 ] ]

    # Test case 3
    mat = [ [1, 2 ],
            [4, 5 ] ]

    '''

    rotateMatrix(mat)

    # Print rotated matrix
    displayMatrix(mat)



