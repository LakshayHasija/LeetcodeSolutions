class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
        if len(nums)==k:
            return max(nums)
        if k==1:
            ans=-1
            for val,freq in freq.items():
                if freq==1:
                    ans=max(ans,val)
            return ans
        if freq[nums[0]]==1 and freq[nums[-1]]==1:
            return max(nums[0],nums[-1])
        elif freq[nums[0]]==1:
            return nums[0]
        elif freq[nums[-1]]==1:
            return nums[-1]
        else:
            return -1