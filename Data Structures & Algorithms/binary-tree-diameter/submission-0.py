# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root):
            nonlocal diameter 

            hr = 0 
            hl = 0

            if root == None:
                return 0
            if root.right != None:
                hr += height(root.right)
            if root.left != None:
                hl += height(root.left)
            diameter = max(hr + hl, diameter)
            return max(hr, hl) + 1
        
        height(root)
        return diameter

            


        