class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        safe=[False]*n
        visited=[False]*n
        def dfs(node):
            if visited[node]:
                return safe[node]
            visited[node]=True
            for i in graph[node]:
                if not dfs(i):
                    return False
            safe[node]=True
            return True
        result=[]
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result