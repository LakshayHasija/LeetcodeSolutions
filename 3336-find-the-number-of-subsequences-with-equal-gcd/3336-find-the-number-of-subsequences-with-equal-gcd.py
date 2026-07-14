class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        m=max(nums)
        dp=[[0]*(m+1) for _ in range(m+1)]
        dp[0][0]=1

        for i in nums:
            next_dp=[row[:] for row in dp]
            for j in range(m+1):
                for k in range(m+1):
                    if not dp[j][k]:
                        continue
                    n1,n2 = gcd(j,i),gcd(k,i)
                    next_dp[n1][k] = (next_dp[n1][k] + dp[j][k]) % MOD
                    next_dp[j][n2] = (next_dp[j][n2] + dp[j][k]) % MOD
            dp=next_dp
        
        return sum(dp[i][i] for i in range(1,m+1))%MOD