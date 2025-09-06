class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        @lru_cache(None)
        def backtracking(index):
            if index>=n-1:
                return 0
            minsteps=999999999
            for i in range(1,nums[index]+1):
                if index+i<n:
                    step=backtracking(index+i)
                if step!=999999999:
                    minsteps=min(step+1,minsteps)
            return minsteps
        ans=backtracking(0)
        if ans==999999999:
            return -1
        return ans