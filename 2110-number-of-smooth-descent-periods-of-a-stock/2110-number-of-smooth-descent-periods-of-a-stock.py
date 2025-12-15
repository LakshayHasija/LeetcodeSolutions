class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=1
        n=1
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                n+=1
            else:
                n=1
            ans+=n
        return ans