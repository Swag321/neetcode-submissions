# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # have a pointer at beginning, midpoint, and end
        # break the chain to the midpoint
        # move from end to midpoint, reversing each next pointer
        # finally, make left -> right. and move left and right to original next

        s,f = head,head.next
        while f and f.next:
            s,f = s.next, f.next.next
        
        # if we initialize f at head: now s is at midpoint or midpoint + 1, f is at end or end + 1
        # reinitialize f at head.next: now s is at left of midpoint if even or midpoint if odd; f is still end or end+1

        start = s.next # start: where second half starts
        s.next = None # break the chain
        p = None
        while start:
            temp = start.next
            start.next = p
            p = start
            start = temp
        
        # now everything in second half is reversed

        lp, rp = head, p
        while rp:
            # lOriginal, rOriginal = lp.next, rp.next
            # lp.next = rp
            # rp.next = lOriginal
            # lp, rp = lOriginal, rOriginal
            lo = lp.next
            lp.next = rp
            ro = rp.next
            rp.next = lo
            lp,rp = lo,ro
