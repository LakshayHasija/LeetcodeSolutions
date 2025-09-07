class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==0:
            ans=[]
        else:
            ans=[0]
            n-=1    #n is a even number now
        for i in range(1,n//2+1):
            ans.append(i)
            ans.append(i*-1)
        return ans