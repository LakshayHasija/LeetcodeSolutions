class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)    #rows
        m=len(board[0]) #cols
        def dfs(row,col,word_i):
            if row<0 or row>=n or col<0 or col>= m:
                return False
            if board[row][col]!=word[word_i]:
                return False
            if word_i==len(word)-1:
                return True
            temp=board[row][col]
            board[row][col] ='#'  # mark visited
            if row>0 and dfs(row-1,col,word_i+1):
                return True
            if row<n-1 and dfs(row+1,col,word_i+1):
                return True
            if col>0 and dfs(row,col-1,word_i+1):
                return True
            if col<m-1 and dfs(row,col+1,word_i+1):
                return True
            board[row][col] = temp  # backtrack
            return False
        cond=False
        for i in range(n):
            for j in range(m):
                cond=cond or dfs(i,j,0)
                if cond==True:
                    return True
        return False