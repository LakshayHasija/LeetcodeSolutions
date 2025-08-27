class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=len(g)-1  #no of childs and desire and size he can eat in g
        j=len(s)-1  #no of cookies and there size in s
        g.sort()
        s.sort()
        ans=0
        while i>=0 and j>=0:
            if g[i]<=s[j]:
                ans+=1
                i-=1
                j-=1
            else:
                i-=1
        return ans