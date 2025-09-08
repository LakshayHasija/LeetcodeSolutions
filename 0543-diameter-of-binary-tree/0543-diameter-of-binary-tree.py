# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        temp=[0]
        def helper(node):
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            temp[0]=max(temp[0],1+left+right)
            return 1+max(left,right)
        helper(root)
        return temp[0]-1