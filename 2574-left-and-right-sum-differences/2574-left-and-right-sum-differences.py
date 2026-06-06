class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        leftsum=[0]
        rightsum=[0]
        n=len(nums)
        for i in range(len(nums)-1):
            leftsum.append(nums[i]+leftsum[-1])
        for i in range(n-1,0,-1):
            rightsum.append(nums[i]+rightsum[-1])
        rightsum.reverse()
        for i in range(len(leftsum)):
            ans.append(abs(rightsum[i]-leftsum[i]))
        return ans