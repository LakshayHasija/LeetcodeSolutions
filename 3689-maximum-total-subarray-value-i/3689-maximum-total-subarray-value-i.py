class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        small=large=nums[0]
        for n in nums:
            small=min(small,n)
            large=max(large,n)
        return (large-small)*k