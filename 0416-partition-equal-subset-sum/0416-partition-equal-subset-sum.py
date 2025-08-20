class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_=sum(nums)
        if sum_%2==1:
            return False
        target=sum_//2
        dp=[[False]*(target + 1) for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if j==0:
                    dp[i][j]=True
                elif i==0:
                    dp[i][j]=False
        for i in range(1,n+1):
            for j in range(1,target+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][target]