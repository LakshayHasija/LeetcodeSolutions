class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        maxi=0
        for i in nums:
            if i==1:
                c+=1
                maxi=max(maxi,c)
            else:
                c=0
        return maxi