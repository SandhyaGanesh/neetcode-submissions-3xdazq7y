# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the length of the Linked List
        if not head or not head.next:
            return 

        start = head
        l = 0
        while start:
            l += 1
            start = start.next
        
        # Split the linked list into half
        newHead = head
        hl = l//2
        while hl > 0:
            temp = newHead.next
            if hl == 1:
                newHead.next = None
            newHead = temp
            hl -= 1
        
        # reverse the second half
        newHead = self.reverseList(newHead)

        dummyHead = ListNode()
        retHead = dummyHead
        while head and newHead:
            dummyHead.next = head
            head = head.next
            dummyHead = dummyHead.next
            dummyHead.next = newHead
            newHead = newHead.next
            dummyHead = dummyHead.next
            
        
        if head:
            dummyHead.next = newHead
            dummyHead = dummyHead.next
        if newHead:
            dummyHead.next = newHead
        head = retHead.next
        