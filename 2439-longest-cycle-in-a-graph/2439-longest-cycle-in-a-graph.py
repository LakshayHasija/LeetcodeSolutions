class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        visited=[False]*n
        answer=-1
        for i in range(n):
            if visited[i]:
                continue
            path={}
            node=i
            curr=0
            while node!=-1:
                if node in path:
                    temp=curr-path[node]
                    answer=max(answer,temp)
                    break
                if visited[node]:
                    break
                path[node]=curr
                visited[node]=True
                node=edges[node]
                curr+=1
        return answer