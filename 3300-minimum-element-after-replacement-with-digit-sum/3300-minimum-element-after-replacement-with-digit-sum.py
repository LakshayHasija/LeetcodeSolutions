class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=100
        for i in nums:
            i=str(i)
            curr_sum=0
            for j in range(len(i)):
                curr_sum+=int(i[j])
            ans=min(ans,curr_sum)
        return ans