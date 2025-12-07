class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=high-low
        if low%2==0:
            return (count+1)//2
        else:
            return count//2+1