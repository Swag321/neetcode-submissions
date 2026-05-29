# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None #null
        node = head #0

        #reverse current node's next pointer
        while node:
            temp = node.next # temp: 1 | prev: 2
            node.next = prev # 0 -> null | 1 -> 0 -> null
            prev = node # prev: 0 -> null | prev: 1 -> 0 -> null
            node = temp #node: 1 | node: 2
        
        return prev
            
