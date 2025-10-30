class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans=0
        prev=0
        for i in target:
            if i>prev:
                ans+=i-prev
            prev=i
        return ans