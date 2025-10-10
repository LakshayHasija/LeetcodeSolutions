class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n=len(energy)
        sums=[-float("inf")]*n
        for i in range(n-1,-1,-1):
            if sums[i]==-float("inf"):
                temp=0
                j=i
                while j>=0:
                    temp+=energy[j]
                    # print(i,j,temp)
                    sums[j]=temp
                    j-=k
        # print(sums)
        return max(sums)