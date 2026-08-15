class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_val=0
        all_zeros=True  #lets assume all elements are 0
        for i in nums:
            xor_val^=i  #calculate xor for each element
            if i!=0:
                all_zeros=False
        if xor_val!=0:
            return len(nums)
        if not all_zeros:
            return len(nums)-1
        return 0