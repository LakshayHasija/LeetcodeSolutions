class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        b=len(height)-1
        ans=0
        while a<b:
            if height[a]<height[b]:
                temp=height[a]*(b-a)
                a+=1
            else:
                temp=height[b]*(b-a)
                b-=1
            ans=max(temp,ans)
        return ans
