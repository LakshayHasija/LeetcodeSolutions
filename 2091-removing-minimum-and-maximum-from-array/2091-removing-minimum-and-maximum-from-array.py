class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return n
        high_idx=max(nums.index(max(nums)),nums.index(min(nums)))
        low_idx=min(nums.index(max(nums)),nums.index(min(nums)))
        return min(max(high_idx,low_idx)+1,max(n-high_idx,n-low_idx),low_idx+1+n-high_idx)