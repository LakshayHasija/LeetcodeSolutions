class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=b=0
        for n in nums:
            pa, pb = a, b
            a = max(a, n)
            b = max(b, min(pa, n))
        return (a-1)*(b-1)