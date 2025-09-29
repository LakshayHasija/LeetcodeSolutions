# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums=defaultdict(int)
        prefix_sums[0]=1
        count=0
        def dfs(node,current_sum):
            nonlocal count
            if not node:
                return
            current_sum+=node.val
            count += prefix_sums[current_sum - targetSum]
            prefix_sums[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1
        dfs(root, 0)
        return count