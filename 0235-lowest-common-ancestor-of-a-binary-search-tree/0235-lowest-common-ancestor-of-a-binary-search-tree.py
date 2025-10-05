# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath=[]
        qpath=[]
        def dfs(node,path):
            nonlocal ppath, qpath
            if not node:
                return
            if node==p:
                ppath=path[:]
            if node==q:
                qpath=path[:]
            if ppath and qpath:
                return
            path.append(-1)
            dfs(node.left,path)
            path.pop()
            path.append(1)
            dfs(node.right,path)
            path.pop()
        dfs(root,[0])
        curr=root
        for i in range(min(len(ppath),len(qpath))):
            if ppath[i]==qpath[i]:
                if ppath[i]==-1:
                    curr=curr.left
                if ppath[i]==1:
                    curr=curr.right
            else:
                break
        return curr