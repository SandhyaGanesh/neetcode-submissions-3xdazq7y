# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        print("Printy")
        while head:
            print(head.val)
            head = head.next
        
        
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newHead = curr = ListNode()
        nl1 = l1
        nl2 = l2
        # nl1 = self.reverseList(l1)
        # nl2 = self.reverseList(l2)

        test = ListNode(6)
        print(test)
        test = None
        print(test)
        prev = None
        while nl1 or nl2:
            v1 = nl1.val if nl1 else 0
            v2 = nl2.val if nl2 else 0
            sumv = v1 + v2 + carry
            carry = sumv // 10
            newVal = sumv % 10
            print(sumv, carry, newVal)
            curr.val = newVal
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            print("curr", curr.val)
            nl1 = nl1.next if nl1 else None
            nl2 = nl2.next if nl2 else None
        
        if carry != 0:
            curr.val = carry
        else:
            print("No carry")
            prev.next = None
            curr = None
        self.printList(newHead)
        return newHead

