# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow = self.reverseList(slow)
        fast = head
        
        while slow:
            if not slow.val == fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
    
    def reverseList(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev