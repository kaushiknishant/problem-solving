def set_zeroes(matrix):
    col0 = True
    rows = len(matrix)
    cols = len(matrix[0])

    for i in xrange(0,rows):
        if matrix[i][0] == 0:
            col0 = False
        for j in xrange(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    
    for i in xrange(rows-1, -1, -1):
        for j in xrange(cols-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == False:
            matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    set_zeroes(matrix)
    print(matrix)