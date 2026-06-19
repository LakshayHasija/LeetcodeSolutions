class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=[0]
        for i in range(len(gain)):
            alt.append(gain[i]+alt[-1])
        return max(alt)