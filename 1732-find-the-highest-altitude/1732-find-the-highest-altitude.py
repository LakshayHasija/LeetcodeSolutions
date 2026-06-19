class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt,ans=0,0
        for i in gain:
            alt+=i
            ans=max(ans,alt)
        return ans