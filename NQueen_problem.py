from __future__ import print_function
def is_board_safe(board,row,col,n):
    for i in range(n):
        if board[row][i] == 1:
            return False

    for i in range(n):
        if board[i][col] == 1:
            return False

    x = row
    y = col
    while(x >= 0 and y >= 0):
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1
    
    x = row
    y = col  
    while(x >= 0 and y < n):
        if board[x][y] == 1:
            return False
        x -= 1
        y += 1
  
    return True

def solve_n_queen(board,i,n):
    if i == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("Q",end=" ")
                else:
                    print("_",end=" ")
            print()
        return True
    
    for j in range(n):
        if is_board_safe(board,i,j,n):
            board[i][j] = 1
            place_next_queen = solve_n_queen(board,i+1,n)
            if place_next_queen:
                return True
            board[i][j] = 0
    return False

if __name__ == '__main__':
    n = 4
    board = [[0]*n for _ in range(n)]
    solve_n_queen(board,0,n)   