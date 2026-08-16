class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        divisi=[0,0,0]
        for i in stones:
            rem=i%3
            if rem==0:
                divisi[2]+=1
            elif rem==2:
                divisi[1]+=1
            else:
                divisi[0]+=1
        if divisi[2]%2==0:
            return divisi[0]>=1 and divisi[1]>=1
        return abs(divisi[0]-divisi[1])>2