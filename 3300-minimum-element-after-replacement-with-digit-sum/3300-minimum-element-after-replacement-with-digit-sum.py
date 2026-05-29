class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=sys.maxsize
        for i in range(len(nums)):
            a=0
            while nums[i]>0:
                a+=nums[i]%10
                nums[i]//=10
            ans=min(ans,a)
        return ans