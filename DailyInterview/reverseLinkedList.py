class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    # Implement this.
    if not head or not head.next:
        return head
        
    root = ListNode(head.val)
    while head.next:
        new_root = ListNode(head.next.val)
        new_root.next = root
        root = new_root
        head = head.next
    return root

  # Recursive Solution      
  def reverseRecursively(self, head):
    # Implement this.
    if not head or not head.next:
            return head
        
    new_root = self.reverseRecursively(head.next)
    head.next.next = head
    head.next = None
    return new_root

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0

testHead = testHead.reverseIteratively(testHead)
print("List after iterative reversal: ")
testHead.printList()
# 0 1 2 3 4

testHead = testHead.reverseRecursively(testHead)
print("List after recursive reversal: ")
testHead.printList()
# 4 3 2 1 0
