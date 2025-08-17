class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if maxPts+k<=n:
            return 1.0
        prob=[0]*(k-1+maxPts+1)
        for i in range(k,n+1):
            prob[i]=1
        total=n+1-k
        for i in range(k-1,-1,-1):
            prob[i]=total/maxPts
            total-=prob[i+maxPts]
            total+=prob[i]
        return prob[i]