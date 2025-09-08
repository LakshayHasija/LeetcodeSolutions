# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        temp=[-9999]
        def helper(node):
            if not node:
                return 0
            left=max(helper(node.left),0)
            right=max(helper(node.right),0)
            temp[0]=max(temp[0],
            node.val+left+right,
            node.val,
            node.val+max(left,right))
            return node.val+max(left,right)
        helper(root)
        return temp[0]