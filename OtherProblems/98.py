# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        left_side_largest = -2**31-1

        while root or len(stack) > 0:
            ## iterate way left down if there is left node
            while root:
                stack.append(root)
                root = root.left
            
            ## start inorder iterating
            root = stack.pop()
            ## check if the root is greater than the largest number of left side nodes
            if root.val <= left_side_largest:
                ## if not return false
                return False
            left_side_largest = root.val
            root = root.right
        
        return True


'''
Inorder Recursive

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.left_side_largest:
                return False
            self.left_side_largest = root.val
            return inorder(root.right)

        self.prev = -2**31-1
        return inorder(root)
'''