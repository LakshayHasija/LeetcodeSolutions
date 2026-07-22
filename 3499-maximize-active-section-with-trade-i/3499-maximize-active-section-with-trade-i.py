class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        s="1"+s+"1"
        total=s.count('1')-2
        l=m=r=0
        temp=0
        i=0
        n=len(s)
        while i<n:
            if s[i] =='0':
                if m==0:
                    l+=1
                else:
                    r+=1
            else:
                if r>0:
                        temp=max(temp,l+r)
                        l=r
                        m=1
                        r=0
                elif l>0:
                        m+=1
            i+=1
        return min(n-2,temp+total)
                