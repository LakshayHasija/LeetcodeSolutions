class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        commas=0
        start=1000
        while start<=n:
            commas+=n-start+1
            start*=1000
        return commas