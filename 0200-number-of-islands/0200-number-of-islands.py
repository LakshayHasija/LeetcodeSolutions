class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid) #row
        m=len(grid[0]) #col
        visited=[[False for _ in range(m)] for _ in range(n)]
        islands=0
        def dfs(row,col):
            if visited[row][col]:
                return
            visited[row][col]=True
            if grid[row][col]=="0":
                return
            if row>0: #up
                dfs(row-1,col)
            if row<n-1:  #down
                dfs(row+1,col)
            if col>0:  #left
                dfs(row,col-1)
            if col<m-1:  #right
                dfs(row,col+1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and visited[i][j]==False:
                    dfs(i,j)
                    islands+=1
        return islands
