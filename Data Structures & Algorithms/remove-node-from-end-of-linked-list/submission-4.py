# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        p1 = head
        while n > 0:
            n -= 1
            p1 = p1.next
        
        p2 = head
        prev = None
        while p1:
            p1 = p1.next
            prev = p2
            p2 = p2.next
        if prev:
            prev.next = p2.next
        else:
            return p2.next
        
        return head

