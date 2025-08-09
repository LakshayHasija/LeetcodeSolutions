class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=1
        for i in range(31):
            if a==n:
                return True
            a=a*2
        return False