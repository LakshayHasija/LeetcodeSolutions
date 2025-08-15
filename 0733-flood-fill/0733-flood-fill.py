class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image) #rows
        m=len(image[0]) #cols
        oldcolor=image[sr][sc]
        def dfs(row,col):
            if image[row][col]==color:
                return
            if image[row][col]!=oldcolor:
                return
            image[row][col]=color
            if row>0: #up
                dfs(row-1,col)
            if row<n-1:  #down
                dfs(row+1,col)
            if col>0:  #left
                dfs(row,col-1)
            if col<m-1:  #right
                dfs(row,col+1)
        dfs(sr,sc)
        return image
            