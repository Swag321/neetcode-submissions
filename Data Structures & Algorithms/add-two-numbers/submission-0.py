# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 5 3 
        # 4 5 6
        
        # 351
        # 654
        #  1005
        # 5, 0, 0, 1

        # add each node, take the carryover, and append carryover if >0
        result = ListNode()
        dummy = result # is this fine or do we need to do dummy = ListNode(next=result) and later return dummy.next?
        carry = 0
        while l1 or l2:
            result.next = ListNode(val = carry)
            result = result.next
            if l1 and l2:
                total = l1.val + l2.val + result.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val + result.val
                l1 = l1.next
            elif l2:
                total = l2.val + result.val
                l2 = l2.next
            carry = total // 10 # 28//10= 2 (max total can be is 27)
            nodeVal = total % 10 #28%10 = 8
            result.val = nodeVal
        
        if carry > 0:
            result.next = ListNode(carry)
            
        return dummy.next




