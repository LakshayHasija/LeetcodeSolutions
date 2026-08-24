class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)
        s=[0]
        for i in stones:
            s.append(s[-1]+i)
        s.pop(0)
        def recursion(i):
            if i==n-1:
                return s[n-1]
            temp=recursion(i+1)
            return max(temp,s[i]-temp)
        return recursion(1)