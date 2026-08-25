class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp=k
        while True:
            if temp in nums:
                temp+=k
            else:
                return temp