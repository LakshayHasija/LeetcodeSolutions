class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        for i in nums:
            if i in freq:
                return i
            freq[i]+=1