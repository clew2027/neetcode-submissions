# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root == None:
                return 0
            hr = height(root.right)
            hl = height(root.left)
            if hr == -1 or hl == -1:
                return -1
            if abs(hr - hl) > 1:
                return -1
            else: 
                return 1 + max(hr, hl)

        if height(root) == -1:
            return False
        else: 
            return True