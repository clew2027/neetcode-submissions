# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None: 
            return False
        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None and root == None:
            return True
        elif subRoot !=None and root!=None:

            if root.val == subRoot.val:
                return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot) or self.isSameTree(root, subRoot)
            else:
                return self.isSubtree(root.left, subRoot) or self.isSameTree(root, subRoot)
            
        else:
            return False