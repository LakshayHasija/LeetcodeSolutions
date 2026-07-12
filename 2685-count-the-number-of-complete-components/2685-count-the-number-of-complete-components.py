class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False]*n
        graph=defaultdict(list)
        ans=0
        for v,u in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node):
            visited[node]=True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                component=[]
                dfs(i)
                vertices=len(component)
                #sum of degrees/2=edges
                edge_count=sum(len(graph[x]) for x in component)//2
                if edge_count==vertices*(vertices-1)//2:
                    ans+=1
        return ans