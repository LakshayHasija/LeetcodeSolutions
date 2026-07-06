class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        ans=r=0
        for i,j in intervals:
            if j>r:
                ans+=1
            r=max(r,j)
        return ans