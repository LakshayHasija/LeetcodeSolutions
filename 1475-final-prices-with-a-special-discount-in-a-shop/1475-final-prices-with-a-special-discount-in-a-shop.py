class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            while stack and prices[i]<prices[stack[-1]]:
                stack.pop()
            if stack:
                ans[i]=prices[i]-prices[stack[-1]]
            else:
                ans[i]=prices[i]
            stack.append(i)
        return ans