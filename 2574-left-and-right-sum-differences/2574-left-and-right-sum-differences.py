class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=0
        right_sum=sum(nums)
        ans=[]
        for i in nums:
            right_sum-=i 
            ans.append(abs(left_sum-right_sum))
            left_sum+=i
        return ans