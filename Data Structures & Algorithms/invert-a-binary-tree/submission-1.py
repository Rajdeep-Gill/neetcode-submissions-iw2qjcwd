# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = deque()
        q.append([root])
        while q:
            curr = q.popleft()
            next_layer = []
            for i in range(len(curr)):
                temp = curr.pop()

                temp.left, temp.right = temp.right, temp.left
                if temp.left:
                    next_layer.append(temp.left)
                if temp.right:
                    next_layer.append(temp.right)
            if next_layer != []:
                q.append(next_layer)

        return root
            

        # def invert(root):
        #     if not root:
        #         return

        #     root.left, root.right = root.right, root.left
        #     invert(root.left)
        #     invert(root.right)


        # invert(root)
        # return root