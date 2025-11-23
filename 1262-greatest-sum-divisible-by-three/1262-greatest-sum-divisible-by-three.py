class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0,float('-inf'),float('-inf')]
        for num in nums:
            new_dp = dp[:]
            for i in range(3):
                new_remainder = (i + num) % 3
                new_dp[new_remainder] = max(new_dp[new_remainder], dp[i] + num)
            dp = new_dp
        return dp[0]