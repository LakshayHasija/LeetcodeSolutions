class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq=Counter(nums)
        missing,duplicate=None,None
        for i in range(1,len(nums)+1):
            if i not in freq:
                missing=i
            if freq[i]==2:
                duplicate=i
            if missing and duplicate:
                return [duplicate,missing]
