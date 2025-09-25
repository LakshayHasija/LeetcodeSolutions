class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height=len(triangle)
        dp = [[None] * len(row) for row in triangle]
        def helper(level,idx):
            if level==height-1:
                return triangle[level][idx]
            if dp[level][idx] is not None:
                return dp[level][idx]
            same=helper(level+1,idx)
            notsame=helper(level+1,idx+1)
            dp[level][idx]=triangle[level][idx]+min(same,notsame)
            return dp[level][idx]
        return helper(0,0)