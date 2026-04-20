def solveSudoku(board):
    def canWePlace(row,col,num,board):
        for i in range(0,n):
            if(board[row][i]==num or board[i][col]==num):
                return False
        #sub grid
        start_row,start_col=3*(row//3),3*(col//3)
        for i in range(start_row,start_row+3):
            for j in range(start_col,start_col+3):
                if(board[i][j]==num):
                    return False
        return True
    n=9 #no of rows and cols
    def solve(board):
        for row in range(0,n):
            for col in range(0,n):
                if(board[row][col]=='.'):
                    for num in '123456789':
                        if(canWePlace(row,col,num,board)):
                            board[row][col]=num
                            if(solve(board)):
                                return True
                            board[row][col]='.'
                    return False
        return True
    return solve(board)
board=[]
for lst in range(0,9):
    lst=list(map(str,input().split()))
if(solveSudoku(board)):
    print(board)
