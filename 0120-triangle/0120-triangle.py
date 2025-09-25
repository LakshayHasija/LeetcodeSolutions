class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height=len(triangle)
        @lru_cache(None)
        def helper(level,idx):
            if level==height:
                return 0
            same=triangle[level][idx]+helper(level+1,idx)
            notsame=triangle[level][idx+1]+helper(level+1,idx+1)
            return min(same,notsame)
        return helper(1,0)+triangle[0][0]