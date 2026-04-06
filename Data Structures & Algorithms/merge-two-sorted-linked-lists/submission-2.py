# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        p1 = list1
        p2 = list2
        newHead = ListNode()
        curr = newHead

        while p1 and p2:
            if p1.val > p2.val:
                curr.next = p2
                p2 = p2.next
            else:
                curr.next = p1
                p1 = p1.next
            curr = curr.next
        
        while p1:
            curr.next = p1
            p1 = p1.next
            curr = curr.next

        while p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next
        return newHead.next