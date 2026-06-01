class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans=0
        free=0
        for i in cost:
            if free==2:
                free=0
                continue
            free+=1
            ans+=i
        return ans