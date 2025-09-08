class Solution:
    def superEggDrop(self, eggs: int, floors: int) -> int:
        dp=[[-1]*(floors+1) for i in range(eggs+1)]
        def helper(eggs,floors):
            if floors==0 or floors==1 or eggs==1:
                return floors
            if eggs==0:
                return 0
            if dp[eggs][floors]!=-1:
                return dp[eggs][floors]
            bottom=1
            top=floors
            ans=9999999
            while bottom<=top:
                mid=(bottom+top)//2
                breaks=helper(eggs-1,mid-1)
                saves=helper(eggs,floors-mid)
                worst=1+max(breaks,saves)
                if breaks>saves:
                    top=mid-1
                else:
                    bottom=mid+1
                ans=min(ans,worst)
            dp[eggs][floors]=ans
            return ans
        return helper(eggs,floors)