# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass -> to end
        # l and r pointer with r all the way to end keep i++
        l = head
        i = 0
        r = head
        
        while r:
            i += 1
            r = r.next
        
        #could be done one pass with slow fast pointers acc
        # if i == 1:
        #     return None
        target = i - n #target to disconnect prior node
        if not head:
            return None
        elif target == 0:
            return head.next
            
        j = 1
        while j < target:
            l = l.next
            j += 1
        
        l.next = l.next.next if l.next else None #skip nth

        return head


            

