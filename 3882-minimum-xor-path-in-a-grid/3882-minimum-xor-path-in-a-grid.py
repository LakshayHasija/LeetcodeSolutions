class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp = [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    prev = {0}
                else:
                    prev = set(dp[j])
                    if j > 0:
                        prev.update(dp[j - 1])
                dp[j] = {x ^ grid[i][j] for x in prev}
        return min(dp[n - 1])