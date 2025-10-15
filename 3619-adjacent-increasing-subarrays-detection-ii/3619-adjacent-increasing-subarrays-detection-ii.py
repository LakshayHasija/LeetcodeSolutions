class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans=1
        if len(nums)==2:
            return 1
        if nums[0]<nums[1]:
            i=0
        else:
            i=1
        j=1
        adj=[]
        while j<len(nums):
            while j<len(nums) and nums[j-1]<nums[j]:
                j+=1
            if i!=j-1:
                ans=max(ans,(j-i)//2)
                if adj and adj[-1][1]+1==i:
                    ans=max(ans,min((adj[-1][1]-adj[-1][0])+1,j-i))
                adj.append([i,j-1])
            i=j
            j+=1
        print(adj)
        return ans