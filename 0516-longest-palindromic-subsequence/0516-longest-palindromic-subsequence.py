class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[-1] * 1001 for _ in range(1001)]
        def helper(first,last):
            if first>last:
                return 0
            if dp[first][last]!=-1:
                return dp[first][last]
            if s[first]==s[last]:
                ans=helper(first+1,last-1)+2
                if first==last:
                    ans-=1
            else:
                ans=max(helper(first+1,last),helper(first,last-1))
            dp[first][last]=ans
            return ans
        return helper(0,len(s)-1)