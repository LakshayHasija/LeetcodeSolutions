class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for i,s in enumerate(score):
            heapq.heappush(heap,(-s,i))
        ans=['' for _ in range(len(score))]
        rank=1
        while heap:
            _,idx=heapq.heappop(heap)
            if rank==1:
                ans[idx]="Gold Medal"
            elif rank==2:
                ans[idx]="Silver Medal"
            elif rank==3:
                ans[idx]="Bronze Medal"
            else:
                ans[idx]=str(rank)
            rank+=1
        return ans