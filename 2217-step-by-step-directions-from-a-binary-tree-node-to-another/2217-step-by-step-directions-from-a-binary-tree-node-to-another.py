# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startpath=[]
        destpath=[]
        def dfs(root,temp):
            if not root:
                return
            if root.val==startValue:
                startpath.extend(temp[:])
            if root.val==destValue:
                destpath.extend(temp[:])
            temp.append('L')
            dfs(root.left,temp)
            temp.pop()
            temp.append('R')
            dfs(root.right,temp)
            temp.pop()
        dfs(root,[])
        i=0
        while i<len(startpath) and i<len(destpath) and startpath[i]==destpath[i]:
            i+=1
        return 'U'*(len(startpath)-i)+''.join(destpath[i:])