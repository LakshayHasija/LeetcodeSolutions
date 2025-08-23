class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[99999 for i in range(amount+1)]for i in range(len(coins)+1)]
        if amount==0:
            return 0
        for i in range(len(coins)+1):
            dp[i][0]=0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        n=dp[len(coins)][amount]
        if n==99999:
            return -1
        return n