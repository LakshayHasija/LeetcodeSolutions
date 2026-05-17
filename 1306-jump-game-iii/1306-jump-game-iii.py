class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=[0]*len(arr)
        def helper(i):
            if i<0 or i>len(arr)-1 or visited[i]==1:
                return False
            if arr[i]==0:
                return True
            visited[i]=1
            right=helper(i+arr[i])
            left=helper(i-arr[i])
            if left or right:
                return True
            return False
        return helper(start)