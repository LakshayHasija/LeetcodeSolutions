class Solution:
    def ispalandrom(self,s):
        return s==s[::-1]
    def minCut(self, s: str) -> int:
        dp=[-1]*(len(s)+1)
        def solve(i,j):
            if i>=j:
                return 0
            if self.ispalandrom(s[i:j+1]):
                return 0
            if dp[i]!=-1:
                return dp[i]
            mincuts=999999999
            for k in range(i,j):
                if self.ispalandrom(s[i:k+1]):
                    cuts=solve(k+1,j)+1
                    mincuts=min(mincuts,cuts)
            dp[i]=mincuts
            return mincuts
        return solve(0,len(s)-1)