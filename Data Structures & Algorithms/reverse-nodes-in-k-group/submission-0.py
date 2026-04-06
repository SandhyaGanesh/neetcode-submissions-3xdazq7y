# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = curr = head
        prev = dummyHead
        while curr:
            groupHead = curr
            counter = k
            while curr and counter > 1:
                curr = curr.next
                counter -= 1
            if curr:
                temp = curr.next
                curr.next = None
                newHead = self.reverseList(groupHead)
                prev.next = newHead
                groupHead.next = temp
                prev = groupHead
                curr = temp
            else:
                break
        return dummyHead.next