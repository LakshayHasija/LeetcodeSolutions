# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        def helper(l, r):
            if l>r:
                return [None]
            trees=[]
            for i in range(l,r+1):
                left_subtrees=helper(l,i-1)
                right_subtrees=helper(i+1,r)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root=TreeNode(i)
                        root.left=left
                        root.right=right
                        trees.append(root)
            return trees
        return helper(1,n)