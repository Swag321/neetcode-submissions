# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        s,f = head, head.next

        while f and f.next:
            if s == f:
                return True
            s,f = s.next, f.next.next
        
        # by this point we conclude there's no cycle
        return False