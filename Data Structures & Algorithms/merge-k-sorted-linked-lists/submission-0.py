# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoSortedLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        curr = dummyHead = ListNode()
        l1 = list1
        l2 = list2
        while l1 or l2:
            if not l1:
                curr.next = l2
                break
            if not l2:
                curr.next = l1
                break
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next   
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dummyHead.next
                
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        print(lists)
        
        if l == 0:
            return None
        elif l == 1:
            return lists[0]
        elif l == 2:
            return self.mergeTwoSortedLists(lists[0], lists[1])

        i = 0
        e = l - 1
        m = (i+e) // 2
        return self.mergeTwoSortedLists(self.mergeKLists(lists[i:m + 1]), self.mergeKLists(lists[m + 1:e+1]))
        