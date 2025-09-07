class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        ans=0
        temp=0
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            elif nums[i-1]+1==nums[i]:
                temp+=1
            else:
                temp=0
            ans=max(ans,temp)
        return ans+1