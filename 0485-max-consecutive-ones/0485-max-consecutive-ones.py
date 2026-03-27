class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=0
        ans=0
        temp=0
        while n<len(nums):
            if nums[n]==1:
                temp+=1
            else:
                temp=0
            ans=max(ans,temp)
            n+=1
        return ans