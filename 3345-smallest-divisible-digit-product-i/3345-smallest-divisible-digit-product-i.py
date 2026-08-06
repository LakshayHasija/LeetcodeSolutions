class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=1
        units=1
        while True:
            if units<=n:
                digit=(n//units)%10
                i*=digit
                units*=10
            else:
                if i%t==0:
                    return n
                n+=1
                i=1
                units=1