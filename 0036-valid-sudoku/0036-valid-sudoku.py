class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)
        def helper(r,c):
            if r==n:
                return True
            if c==n:
                return helper(r+1,0)
            if board[r][c]!=".":
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]: # check if repeated in row,col or sqaure
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r//3,c//3].add(board[r][c])
                    return helper(r,c+1)
            else:
                return helper(r,c+1)
        return helper(0,0)