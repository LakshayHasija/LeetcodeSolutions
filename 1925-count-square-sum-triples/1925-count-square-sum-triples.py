class Solution:
    def countTriples(self, n: int) -> int:
        sq = {i*i for i in range(1, n+1)}
        r = 0
        for i in range(1, n+1):
            temp = i*i
            for j in range(i+1, n+1):
                s = temp + j*j
                if s in sq:
                    r += 2
        return r