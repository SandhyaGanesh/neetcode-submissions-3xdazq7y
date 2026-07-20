# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        i = 0
        curr = head
        while i < n:
            i += 1
            curr = curr.next
        
        dummyHead = ListNode()
        dummyHead.next = head
        p1 = dummyHead
        p2 = curr
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        return dummyHead.next
