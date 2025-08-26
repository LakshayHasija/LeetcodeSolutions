class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxdiag=[0,0]
        for a,b in dimensions:
            if maxdiag[0]<a**2+b**2:
                maxdiag=[a**2+b**2,a*b]
            elif maxdiag[0]==a**2+b**2:
                if a*b>maxdiag[1]:
                    maxdiag=[a**2+b**2,a*b]
        return maxdiag[1]