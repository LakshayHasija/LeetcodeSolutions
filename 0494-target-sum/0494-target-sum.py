class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None) #this is amazing tool from python - DP without needing to store any input just solve the problem in recursion as i used to do beforehand but there is a drawback- You can’t use lists or dictionaries as arguments they must be immutable types like int, str, tuple. 
        def backtracking(index,tempsum):
            if index==len(nums):
                return 1 if tempsum==target else 0
            return backtracking(index+1,tempsum+nums[index])+backtracking(index+1,tempsum-nums[index])
        return backtracking(0,0)