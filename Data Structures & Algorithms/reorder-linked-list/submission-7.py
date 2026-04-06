# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        # Count number of nodes
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        
        half = math.ceil(cnt / 2)
        
        t1 = head
        t2 = head

        while half > 1:
            t2 = t2.next
            half -= 1

        temp = t2.next
        t2.next = None
        t2 = temp
        
        # reverse t2
        curr = t2
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        t2new = prev

        # interleave both

        p1 = t1
        p2 = t2new

        while p1 and p2:
            print(p1.val, p2.val)
            temp1 = p1.next
            p1.next = p2
            temp2 = p2.next
            p1.next.next = temp1
            p1 = temp1
            p2 = temp2


        