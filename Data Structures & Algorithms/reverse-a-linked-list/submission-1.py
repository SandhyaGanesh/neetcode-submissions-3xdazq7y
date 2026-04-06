# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        prv = None
        nex = head.next

        while cur and nex:
            cur.next = prv
            prv = cur
            cur = nex
            nex = nex.next
        
        cur.next = prv
        
        return cur