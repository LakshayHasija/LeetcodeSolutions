class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_=0
        count=0
        prev=True
        for i in nums:
            if i!=1:
                prev=False
            else:
                if not prev:
                    count=1
                    prev=True
                else:
                    count+=1
            max_=max(max_,count)
        return max_