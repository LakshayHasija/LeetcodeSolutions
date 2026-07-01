class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        r=0
        freq=defaultdict(int)
        ans=0
        while r<len(s):
            freq[s[r]]+=1
            while len(freq)==3:
                ans+=len(s)-r
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            r+=1
        return ans