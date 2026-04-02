# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return (
                same_tree(p.left, q.left) and same_tree(p.right, q.right)
            )

        def dfs(node, target):
            if not node:
                return False
            
            return (
                same_tree(node, target) or
                dfs(node.left, target) or
                dfs(node.right, target)
            )

        return dfs(root, subRoot)