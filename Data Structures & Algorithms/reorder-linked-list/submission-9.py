# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newHead

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        
        s = l // 2
        curr = head
        prev = curr
        while s:
            prev = curr
            curr = curr.next
            s -= 1
        
        prev.next = None
        newHead = self.reverseList(curr)

        dummyHead = ListNode()
        l1 = head
        l2 = newHead
        curr = dummyHead

        while l1 and l2:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        
        if l2:
            curr.next = l2
        
        
