class Solution:
    def kadanes(self,arr):
        maxsum=float('-inf')
        c=0
        i=0
        while i<len(arr):
            c+=arr[i]
            if c<0:
                c=0
            if c>maxsum:
                maxsum=c
            i+=1
        return maxsum if maxsum!=float('-inf') else 0
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        revnums=[nums[i]*-1 for i in range(len(nums))]
        return max(self.kadanes(nums),self.kadanes(revnums))