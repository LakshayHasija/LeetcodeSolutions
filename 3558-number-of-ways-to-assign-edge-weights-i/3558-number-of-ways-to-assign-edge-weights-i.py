class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD=10**9 + 7
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def depthhelper(depth, parent, root):
            maxdepth=depth
            for nei in graph[root]:
                if nei==parent:
                    continue
                maxdepth=max(maxdepth,depthhelper(depth+1,root,nei))
            return maxdepth
        n=depthhelper(0,-1,1)
        return ((2**n)//2)%MOD