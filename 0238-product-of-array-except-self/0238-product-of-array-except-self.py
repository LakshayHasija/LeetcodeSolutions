class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=math.prod(nums)
        if temp==0:
            zeros=[]
            for i in range(len(nums)):
                if nums[i]==0:
                    zeros.append(i)
            if len(zeros)>1:
                return [0]*len(nums)
            else:
                ans=[0]*len(nums)
                left=math.prod(nums[:zeros[0]])
                right=math.prod(nums[zeros[0]+1:])
                ans[zeros[0]]=left*right
                return ans 
        ans=[]
        for i in nums:
            ans.append(temp//i)
        return ans