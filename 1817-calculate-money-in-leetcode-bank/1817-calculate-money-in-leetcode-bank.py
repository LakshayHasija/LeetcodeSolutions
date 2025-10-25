class Solution:
    def totalMoney(self, n: int) -> int:
        start=1
        ans=0
        while n>0:
            if n>=7:
                temp=(7*((2*start)+6))//2
                n-=7
            else:
                temp=n*((2*start)+(n-1))//2
                n=0
            ans+=temp
            start+=1
        return ans