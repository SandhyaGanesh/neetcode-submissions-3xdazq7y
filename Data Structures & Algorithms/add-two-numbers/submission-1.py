# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        ret = c3 = ListNode()
        carry = 0
        while c1 or c2:
            v1 = 0
            v2 = 0
            if c1:
                v1 = c1.val
                c1 = c1.next
            if c2:
                v2 = c2.val
                c2 = c2.next
            val  = v1+v2+carry 
            newval = (val) % 10
            carry = val // 10
            c3.val = newval
            print(c3.val)
            if c1 or c2 or carry:
                c3.next = ListNode()
                c3 = c3.next
        
        if carry > 0:
            c3.val = carry

        return ret