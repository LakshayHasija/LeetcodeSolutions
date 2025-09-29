# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node,val):
            val+=node.val
            if not node.left and not node.right and val==targetSum:
                return True
            left=False
            right=False
            if node.left:
                left=dfs(node.left,val)
            if node.right:
                right=dfs(node.right,val)
            if left or right:
                return True
            return False
        return dfs(root,0)