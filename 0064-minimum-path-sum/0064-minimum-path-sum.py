class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[None for _ in range(m+1)] for _ in range(n+1)]
        def dfs(i,j):
            if dp[i][j] is not None:
                return dp[i][j]
            if i==n-1:
                if j==m-1:
                    dp[i][j]=grid[i][j]
                else:
                    dp[i][j]=grid[i][j]+dfs(i,j+1)
            elif j==m-1:
                dp[i][j]=grid[i][j]+dfs(i+1,j)
            else:
                row=dfs(i+1,j)
                col=dfs(i,j+1)
                dp[i][j]=grid[i][j]+min(row,col)
            return dp[i][j]
        return dfs(0,0)