class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def helper(arr):
            return all(arr[i]<arr[i+1] for i in range(len(arr)-1))
        n = len(nums)
        for i in range(n-2*k+1):
            first=nums[i:i+k]
            second=nums[i+k:i+2*k]
            if helper(first) and helper(second):
                return True
        return False