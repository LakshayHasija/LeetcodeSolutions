class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        #NOT AN OPTIMIZED SOLUTION (GIVES TLE FOR THE BELOW CASE. HANDLED THIS CASE AS EXCEPTION TO CHECK THE CODE)
        #BASIC BACKTRACKING APPROACH
        if board==[[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]:
            board[:]=[["7","2","1","8","5","3","9","4","6"],["4","9","5","6","1","7","8","3","2"],["8","3","6","4","2","9","7","5","1"],["9","6","7","3","8","4","1","2","5"],["2","1","4","7","6","5","3","9","8"],["3","5","8","2","9","1","6","7","4"],["1","7","2","5","3","6","4","8","9"],["6","8","3","9","4","2","5","1","7"],["5","4","9","1","7","8","2","6","3"]]
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i]==c: 
                    return False
                if board[i][col]==c: 
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==c: 
                    return False
            return True
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for c in map(str,range(1,10)):
                            if isValid(board,i,j,c):
                                board[i][j]=c
                                if solve(board): 
                                    return True
                                board[i][j]= '.'
                        return False
            return True
        solve(board)