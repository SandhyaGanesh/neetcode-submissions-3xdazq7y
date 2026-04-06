# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, head)
        firstPointer = dummyHead
        secondPointer = dummyHead

        if not head.next:
            return None

        while n > 0 :
            n -= 1
            firstPointer = firstPointer.next
        
        while firstPointer and firstPointer.next:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        
        if secondPointer and secondPointer.next:
            secondPointer.next = secondPointer.next.next
        else:
            secondPointer.next = None

        return dummyHead.next