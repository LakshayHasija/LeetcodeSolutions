class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge=[True]*n
        for i in range(len(trust)):
            if trust[i][0]!=trust[i][1]:
                judge[trust[i][0]-1]=False
        possible=[]
        for i in range(len(judge)):
            if judge[i]==True:
                possible.append(i)
        for i in possible:
            trustedby=0
            for j in trust:
                if j[1]==i+1:
                    trustedby+=1
            if trustedby==n-1:
                return i+1
        return -1