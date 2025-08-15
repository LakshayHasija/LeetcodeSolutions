class Solution:
    def canFinish(self, v: int, edges: List[List[int]]) -> bool:
        temp=[]
        for _ in range(v):
            temp.append([])
        for i,j in edges:
            temp[i].append(j)
        visited=[0]*v
        stack=[0]*v
        def dfs(v):
            visited[v]=1
            stack[v]=1
            for i in temp[v]:
                if visited[i]==0:
                    if dfs(i):
                        return True
                elif stack[i]==1:
                    return True
            stack[v]=0
            return False
        for i in range(v):
            if visited[i]==0:
                if dfs(i):
                    return False
        return True