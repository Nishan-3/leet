# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]   # global maximum

        def dfs(node):
            if not node:
                return 0

            # max path sum from left & right child
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # path WITH split (update global result)
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # path WITHOUT split (return to parent)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
