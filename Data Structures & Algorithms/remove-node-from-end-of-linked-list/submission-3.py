# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # l,r pointer where r pointer is n nodes ahead
        # this way when r reaches end, l will be at the node to be removed (n nodes behind)
        # when not r, l = l.next.next instead of l.next to skip that node
        dummy = ListNode(next=head)
        l,r = dummy,head
        
        for _ in range(n):
            r = r.next
        
        # at this point r is n-1 ahead of l

        while r:
            r = r.next
            l = l.next
        
        # at this point r is None
        l.next = l.next.next

        return dummy.next
        



