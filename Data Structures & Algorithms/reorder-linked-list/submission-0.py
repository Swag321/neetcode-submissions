# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Have to traverse to the end to capture that node. 
        #keep leftPointer and take rightPointer to the end
        # lPointer.next = rightPointer
        # rightPointer.next (store first before overwriting)= lPointerTemp.next (lPointerTemp = lPointer.next before overwriting)
        # lPointer = lPointerTemp (original next val)
        
        # trick: rp is head of half-reversed list O(n)
        
        lp = head

        # Find midpoint:
        s,f = head, head
        while f and f.next:
            s, f = s.next, f.next.next
        
        midPoint = s

        # MEMORIZE!:
        secondHalf = s.next
        p = None
        s.next = None #disconnect
        s = secondHalf
        while s:
            t = s.next
            s.next = p
            p = s
            s = t
        
        rp = p # set rp to actual end value, which will be in p

        while rp:
            lTemp = lp.next
            lp.next = rp
            rTemp = rp.next
            rp.next = lTemp
            lp,rp = lTemp,rTemp
        
#[1,5,2,4,3]
