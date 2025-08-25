class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for i in range(m+1)]for i in range(n+1)]
        def helper(x,y):
            if x==n or y==m:
                return 0
            if dp[x][y]!=-1:
                return dp[x][y]
            if text1[x]==text2[y]:
                dp[x][y]=1+helper(x+1,y+1)
            else:
                dp[x][y]=max(helper(x+1,y),helper(x,y+1))
            return dp[x][y]
        return helper(0,0) 