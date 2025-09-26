# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for parent_val, child_val, isLeft in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            parent = nodes[parent_val]
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            child = nodes[child_val]
            if isLeft:
                parent.left = child
            else:
                parent.right = child
            children.add(child_val)        
        for val in nodes:
            if val not in children:
                return nodes[val]
        return None