# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getSum(sub_root, sub_str):
            if not sub_root:
                return 0
            elif not sub_root.left and not sub_root.right:
                return int(sub_str+str(sub_root.val))
            else:
                return getSum(sub_root.left, sub_str+str(sub_root.val)) + getSum(sub_root.right, sub_str+str(sub_root.val))
        
        return getSum(root, '')
    
class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getSum(sub_root, sub_num):
            if not sub_root:
                return 0
            elif not sub_root.left and not sub_root.right:
                return sub_num*10 + sub_root.val
            else:
                return getSum(sub_root.left, sub_num*10 + sub_root.val) + getSum(sub_root.right, sub_num*10 + sub_root.val)
        
        return getSum(root, 0)

class Solution3(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_sum = 0
        stack = [(root, 0)]
        
        while stack:
            root, curr_num = stack.pop()
            if root:
                curr_num = curr_num*10 + root.val
                if not root.left and not root.right:
                    root_sum += curr_num
                else:
                    stack.append((root.left, curr_num))
                    stack.append((root.right, curr_num))
        return root_sum