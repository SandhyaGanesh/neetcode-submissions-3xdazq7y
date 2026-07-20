# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseListHelper(self, head):
        if not head:
            return head
        nexx = head.next
        head.next = None
        if nexx:
            (self.reverseListHelper(nexx)).next = head
        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            curr = curr.next
        
        self.reverseListHelper(head)
        return curr

        
        