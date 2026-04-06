"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def printList(self, head):
        print("List")
        while head:
            print(head.val, head.random.val if head.random else "Null")
            head = head.next
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.printList(head)
        curr = head
        while curr:
            newNode = Node(curr.val, curr.next, curr.random)
            curr.next = newNode
            curr = curr.next.next
        
        curr = head
        while curr:
            curr.next.random = curr.next.random.next if curr.next.random else None
            curr = curr.next.next
        
        c1 = head
        c2 = head2 = head.next

        while c1 and c2:
            c1.next = c1.next.next
            c1 = c1.next
            if c2.next:
                c2.next = c2.next.next
            c2 = c2.next
        self.printList(head)
        self.printList(head2)
        return head2
        