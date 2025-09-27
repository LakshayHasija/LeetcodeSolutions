class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n=len(points)
        max_area=0
        for i in range(n-2):
            x,y=points[i]
            for j in range(i+1, n-1):
                b, b1=points[j]
                for k in range(j+1, n):
                    c, c1=points[k]
                    area=(b-x)*(c1-y)-(b1-y)*(c-x)
                    max_area=max(max_area, abs(area))
        return 0.5*max_area