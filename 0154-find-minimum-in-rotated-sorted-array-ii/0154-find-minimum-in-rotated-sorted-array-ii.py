class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[l]==nums[m]==nums[r]:
                l+=1
                r-=1
            elif nums[m]>nums[r]:  # ans in right
                l=m+1
            else:
                r=m
        return nums[l]