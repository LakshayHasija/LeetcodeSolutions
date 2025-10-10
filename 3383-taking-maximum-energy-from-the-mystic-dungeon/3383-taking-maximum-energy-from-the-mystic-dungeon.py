class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        visited=[False]*n
        maxsum=energy[-1]
        for i in range(n-1,-1,-1):
            if not visited[i]:
                temp=0
                j=i
                while j>=0:
                    visited[j]=True
                    temp+=energy[j]
                    j-=k
                    maxsum=max(maxsum,temp)
        return maxsum