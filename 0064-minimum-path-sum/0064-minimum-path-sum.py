class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)-1
        m=len(grid[0])-1
        @lru_cache(None)
        def dfs(i,j):
            if i==n:
                if j==m:
                    return grid[i][j]
                return grid[i][j]+dfs(i,j+1)
            elif j==m:
                return grid[i][j]+dfs(i+1,j)
            else:
                row=dfs(i+1,j)
                col=dfs(i,j+1)
                return grid[i][j]+min(row,col)
        return dfs(0,0)