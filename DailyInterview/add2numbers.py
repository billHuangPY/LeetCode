'''
LC Problem 2

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.


class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        head = ListNode(0)
        ls = head
        while l1 or l2:
            val = ls.val
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:
                ln = ListNode(1)
                ls.val = val - 10
            else:
                ln = ListNode(0)
                ls.val = val

            if not l1 and not l2 and ln.val == 0:
                ln = None

            ls.next = ln
            ls = ln
    
        return head


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(4)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(2)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val)
  result = result.next
# 7 0 8