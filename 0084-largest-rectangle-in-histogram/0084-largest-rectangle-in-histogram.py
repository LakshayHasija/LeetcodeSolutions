class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def prevsmallest(nums):
            stack=[]
            result=[-1]*len(nums)
            for i in range(len(nums)):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    result[i]=stack[-1]
                stack.append(i)
            return result
        def nextsmallest(nums):
            stack=[]
            result=[len(nums)]*len(nums)
            for i in range(len(nums)-1,-1,-1):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    result[i]=stack[-1]
                stack.append(i)
            return result
        
        prev=prevsmallest(heights)
        next=nextsmallest(heights)
        maxarea=0
        for i in range(len(heights)):
            width=next[i]-prev[i]-1
            maxarea=max(maxarea,width*heights[i])
        return maxarea