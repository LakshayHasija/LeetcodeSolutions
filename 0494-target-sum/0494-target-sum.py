class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def backtracking(index,tempsum):
            if index==len(nums):
                return 1 if tempsum==target else 0
            if (index,tempsum) in dp:
                return dp[(index,tempsum)]
            positive=backtracking(index+1,tempsum+nums[index])
            negetive=backtracking(index+1,tempsum-nums[index])
            dp[(index,tempsum)]=positive+negetive
            return dp[(index,tempsum)]
        return backtracking(0,0)