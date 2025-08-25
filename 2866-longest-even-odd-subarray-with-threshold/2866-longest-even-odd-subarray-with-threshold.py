class Solution:
    def custom_and(self, a, b):
        if a == False and b == False:
            return True
        else:
            return a and b
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        c=0
        even=True
        for i in nums:
            if i>threshold:
                c=0
                even=True
                continue
            if self.custom_and(i%2==0,even):
                c+=1
                even=not even
            else:
                if i%2==0:
                    c=1
                    even=False
                else:
                    c=0
                    even=True
            ans=max(ans,c)
        return ans