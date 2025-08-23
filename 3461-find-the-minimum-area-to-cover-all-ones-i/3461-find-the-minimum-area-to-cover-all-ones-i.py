class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top=-1
        bottom=-1
        left=-1
        right=-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if top==-1:
                        top=i
                    bottom=i
                    if left==-1:
                        left=j
                    if right==-1:
                        right=j
                    left=min(left,j)
                    right=max(j,right)
        return (right-left+1)*(bottom-top+1)