class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        remaing_sum=[0]*(n+1)
        for i in range(n-1,-1,-1):
            remaing_sum[i]=remaing_sum[i+1]+piles[i]
        memo={}
        def dfs(curr_pos,M):
            if curr_pos>=n:
                return 0
            if (curr_pos,M) in memo:
                return memo[(curr_pos,M)]
            best=0
            total=remaing_sum[curr_pos]
            piles_left=n-curr_pos
            for X in range(1,min(2*M,piles_left)+1):
                opponent=dfs(curr_pos+X,max(M,X))
                current=total-opponent
                best=max(best,current)
            memo[(curr_pos,M)]=best
            return best
        return dfs(0,1)