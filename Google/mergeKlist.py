from queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = ListNode()
        head = curr
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                q.put((node.next.val, node.next))
        return head.next