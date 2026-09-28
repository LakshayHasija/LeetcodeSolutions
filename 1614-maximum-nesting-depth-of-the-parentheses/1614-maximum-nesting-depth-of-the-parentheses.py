class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i=="(":
                stack.append(i)
                ans=max(ans,len(stack))
            elif i==")":
                stack.pop()
        return ans