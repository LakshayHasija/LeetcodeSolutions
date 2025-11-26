class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD=10**9+7
        m,n=len(grid),len(grid[0])        
        dp=[[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if dp[i][j][r] > 0:
                        if i + 1 < m:
                            dp[i+1][j][(r + grid[i+1][j]) % k] += dp[i][j][r]
                        if j + 1 < n:
                            dp[i][j+1][(r + grid[i][j+1]) % k] += dp[i][j][r]
        return dp[m-1][n-1][0] % MOD