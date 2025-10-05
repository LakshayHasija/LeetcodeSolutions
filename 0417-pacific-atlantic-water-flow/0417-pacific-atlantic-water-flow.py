class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #top/left and bottom/right

        n=len(heights)
        m=len(heights[0])

        pacific=[[False]*m for _ in range(n)]
        atlantic=[[False]*m for _ in range(n)]

        def dfs(r,c,visited,prev_height):
            if (r<0 or r>=n or c<0 or c>=m or visited[r][c] or heights[r][c]<prev_height):
                return
            visited[r][c]=True
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

        for i in range(n):
            dfs(i,0,pacific,heights[i][0])
        for j in range(m):
            dfs(0,j,pacific,heights[0][j])

        for i in range(n):
            dfs(i,m-1,atlantic,heights[i][m-1])
        for j in range(m):
            dfs(n-1,j,atlantic,heights[n-1][j])

        ans=[]

        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans