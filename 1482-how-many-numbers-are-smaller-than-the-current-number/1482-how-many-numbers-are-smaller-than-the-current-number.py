class Solution:
    def binarysearch(self,nums,k):
        l,r=0,len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]==k:
                break
            elif nums[m]>k:
                r=m-1
            else:
                l=m+1
        while m>0 and nums[m]==nums[m-1]:
            m-=1
        # print(m)
        return m
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        nums1=sorted(nums)
        for i in nums:
            # print(nums1,i)
            ans.append(self.binarysearch(nums1,i))
        return ans