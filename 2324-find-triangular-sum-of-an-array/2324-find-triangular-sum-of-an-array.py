class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans=[nums]
        while len(ans[-1])!=1:
            n=len(ans[-1])
            temp=[]
            for i in range(1,n):
                temp.append((ans[-1][i-1]+ans[-1][i])%10)
            ans.append(temp)
        return ans[-1][0]