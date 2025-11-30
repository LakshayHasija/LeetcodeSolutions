class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p     #remove remainder
        if rem == 0:
            return 0
        prefix = 0
        seenNum = {0: -1}   # prefix_sum % p → index
        ans = len(nums)
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem) % p   # what we want to find
            if target in seenNum:
                ans = min(ans, i - seenNum[target])
            seenNum[prefix] = i
        if ans < len(nums): 
            return ans    
        return -1