# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Note: what do you need to save? prev and temp (original next); 
        # then we can redirect current next pointer and move to temp

        prev = None
        while head:
            temp = head.next # save the next node
            head.next = prev # point to prev node
            prev = head # store current head as prev before moving to original next head
            head = temp # make head the original next node (saved)

        #the new head will be null at this point; so we want to return prev
        return prev
