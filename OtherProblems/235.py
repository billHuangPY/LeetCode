# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        while root:
            root_val = root.val
            ## if both nodes are under the left side of root
            if root_val > p_val and root_val > q_val:
                root = root.left
            ## if both nodes are under the right side of root
            elif root_val < p_val and root_val < q_val:
                root = root.right
            ## nodes are seperated by the root or at least overlapped, found the answer
            else:
                return root
        return None