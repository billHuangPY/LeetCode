import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_val = -math.inf
    def maxPathSum(self, root) -> int:
        def get_max(node):
            if not node:
                return 0
            
            max_right = max(get_max(node.right), 0)
            max_left = max(get_max(node.left), 0)
            self.max_val = max(self.max_val, node.val + max_right + max_left)
            return node.val + max(max_right, max_left)
        get_max(root)
        return self.max_val