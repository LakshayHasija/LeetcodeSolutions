class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)-1
        first=nums[0]
        sec=sum(nums)-first
        ans=0
        c=sec-first
        print(c)
        if c%2==0 or c==0:
            ans+=1
        for i in range(1,n):
            first+=nums[i]
            sec-=nums[i]
            c=sec-first
            if c%2==0 or c==0:
                ans+=1
        return ans