# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(root,temp,tempsum):
            nonlocal ans
            if not root:
                return
            temp.append(root.val)
            tempsum+=root.val
            if not root.left and not root.right and tempsum==targetSum:
                ans.append(temp[:])
            else:
                dfs(root.left,temp,tempsum)
                dfs(root.right,temp,tempsum)
            temp.pop()
            return
        dfs(root,[],0)
        return ans