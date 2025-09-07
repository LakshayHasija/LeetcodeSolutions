class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        visited=[0]*len(nums)
        def backtracking(temp,visited):
            if len(temp)==len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if visited[i]==1:
                    continue
                temp.append(nums[i])
                visited[i]=1
                backtracking(temp,visited)
                temp.pop()
                visited[i]=0
        backtracking([],visited)
        return ans