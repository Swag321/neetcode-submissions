# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy to point to newHead
        #create a newHead pointer to point to min(list1,list2 heads) and move that listhead to next
        #while list1 and list2: newHead.next = min(of the two) and move the min list head to next; newHead = newHead.next
        
        head = ListNode()
        dummy = head

        while list1 and list2:

            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else: # list1 >= list2
                head.next = list2
                list2 = list2.next

            head = head.next

        # # at this point either list1 or list2 has ended
        # if list1:
        #     head.next = list1 #fill in head.next with list1 if list1 still exists
        # else:
        #     head.next = list2
        head.next = list1 or list2
        
        return dummy.next # dummy is ours, next is also ours.
