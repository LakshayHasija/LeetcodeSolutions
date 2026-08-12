class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        start=0
        end=-1
        ans=0
        for i in nums:
            end+=1
            freq[i]+=1
            while freq[i]>k:
                freq[nums[start]]-=1
                start+=1
            ans=max(ans,end-start)
        return ans+1