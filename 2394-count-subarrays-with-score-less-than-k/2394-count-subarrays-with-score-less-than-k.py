class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        score=0
        sum_=0 
        cnt=0
        n=len(nums) 
        l=0
        for idx, val in enumerate(nums):
            sum_+=val
            score=sum_*(idx-l+1)
            while score>=k:
                sum_-=nums[l]
                l+=1
                score=sum_*(idx-l+1)
            cnt+=(idx-l+1)
        return cnt