# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if not node:
                return False
            if node.val==target:
                return True
            path.append('L')
            if dfs(node.left,path,target):
                return True
            path.pop()
            path.append('R')
            if dfs(node.right,path,target):
                return True
            path.pop()
            return False
        startPath=[]
        destPath=[]
        dfs(root,startPath,startValue)
        dfs(root,destPath,destValue)
        i=0
        while i<len(startPath) and i<len(destPath) and startPath[i]==destPath[i]:
            i+=1
        return 'U'*(len(startPath)-i)+''.join(destPath[i:])