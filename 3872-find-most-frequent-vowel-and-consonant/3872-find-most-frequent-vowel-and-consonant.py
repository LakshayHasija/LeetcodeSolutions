class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        vowels='aeiou'
        ccount=0
        vcount=0
        for key,frq in freq.items():
            if key in vowels:
                if frq>vcount:
                    vcount=frq
            else:
                if frq>ccount:
                    ccount=frq
        return vcount+ccount