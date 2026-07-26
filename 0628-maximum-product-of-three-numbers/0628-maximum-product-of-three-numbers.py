class Solution:
    def maximumProduct(self, digits: List[int]) -> int:
        digits.sort()
        if len(digits)<2:
            return digits[-1]
        if len(digits)<3:
            return digits[-1]*digits[-2]
        return max(digits[-1]*digits[-2]*digits[-3],digits[-1]*digits[0]*digits[1])