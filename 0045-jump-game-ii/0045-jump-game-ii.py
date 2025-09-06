class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return 0
        goal=n-1
        jumps=0
        farthest=0
        current_end=0
        for i in range(n-1): #0,1,2,3,4
            farthest=max(farthest,i+nums[i])
            if i==current_end:
                jumps+=1
                current_end=farthest
        return jumps