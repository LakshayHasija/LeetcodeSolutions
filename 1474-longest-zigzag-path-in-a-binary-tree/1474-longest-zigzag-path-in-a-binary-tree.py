# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def dfs(node,direction,currheight):
            if not node:
                return
            if currheight>ans[0]:
                ans[0]=currheight
            if direction==-1: #upper left now right
                if node.right:
                    dfs(node.right,1,currheight+1)
                dfs(node.left,-1,1)
            if direction==1: #upper right now left
                if node.left:
                    dfs(node.left,-1,currheight+1)
                dfs(node.right,1,1)
        dfs(root,1,0)
        return ans[0]