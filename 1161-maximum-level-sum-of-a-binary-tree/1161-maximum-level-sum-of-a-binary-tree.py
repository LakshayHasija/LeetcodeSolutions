# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        idx=0
        Sum=-inf
        q=deque()
        q.append(root)
        level=1
        while q:
            n=len(q)
            curSum=0
            for i in range(n):
                Node=q.popleft()
                curSum+=Node.val
                if Node.left: 
                    q.append(Node.left)
                if Node.right: 
                    q.append(Node.right)
            if curSum>Sum:
                idx=level 
                Sum=curSum
            level+=1
        return idx