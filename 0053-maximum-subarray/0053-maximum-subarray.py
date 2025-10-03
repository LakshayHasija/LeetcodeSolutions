class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=-float("inf")
        c=0
        for i in nums:
            c+=i
            maxsum=max(maxsum,c)
            if c<=0:
                c=0
        return maxsum