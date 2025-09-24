class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return ''.join(sorted(list(s)))
        n=len(s)
        ans=s
        for i in range(1,n):
            temp=s[i:]+s[:i]
            ans=min(ans,temp)
        return ans