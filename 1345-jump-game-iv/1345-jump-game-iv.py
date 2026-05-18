class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        num_dict=defaultdict(list)
        for i,j in enumerate(arr):
            num_dict[j].append(i)
        visited=set([0])
        q=deque([(0,0)])  #idx,steps
        while q:
            idx,steps=q.popleft()
            if idx==n-1:    #base condition
                return steps
            neighbors=[]
            if idx-1>=0:
                neighbors.append(idx-1)
            if idx+1<n:
                neighbors.append(idx+1)
            neighbors.extend(num_dict[arr[idx]])
            for i in neighbors:
                if i not in visited:
                    visited.add(i)
                    q.append((i,steps+1))
            num_dict[arr[idx]].clear()  # to avoid repeated processing
        return -1