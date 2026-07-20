"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            nexx = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nexx
            curr = nexx
        
        curr = head
        while curr:
            rand = curr.random
            curr.next.random = rand.next if rand else None
            curr = curr.next.next
        
        c1 = head
        c2 = nh = c1.next

        while c1 and c2:
            c1.next = c1.next.next if c1.next else None
            c1 = c1.next
            c2.next = c2.next.next if c2.next else None
            c2 = c2.next
        
        return nh
    