# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False
        
        if self.sametree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

        #i think first we will use the logic of same tree
    def sametree(self, s: Optional[TreeNode], k: Optional[TreeNode]):
        if not s and not k :
            return True
        if s and k and s.val == k.val:
            return (self.sametree(s.left, k.left) and self.sametree(s.right,k.right)) 
        return False
