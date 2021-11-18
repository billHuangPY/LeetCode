# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum_ = (1 + self.countNodes(root.left)) if root.left else 1
        sum_ += self.countNodes(root.right) if root.right else 0
        return sum_
