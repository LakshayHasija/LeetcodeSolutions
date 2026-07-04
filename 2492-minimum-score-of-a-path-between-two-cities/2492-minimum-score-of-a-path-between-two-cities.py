class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited=[False]*(n+1)
        adj=[[] for _ in range(n+1)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        q=deque([1])
        ans=float('inf')
        while q:
            node=q.popleft()
            for i,j in adj[node]: # i -> neighbor, j -> dist
                ans=min(ans,j)
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
        return ans