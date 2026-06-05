"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #hashmap {Node(val,random): Node(next), Node2: nextNode}
        originalToCopy = {None:None}

        # take the val from original and put into copy node, do same for next, and random.
        # then return head of copy: return originalToCopy[head]
        node = head

        # this intitializes all nodes
        while node:
            copy = Node(node.val)
            originalToCopy[node] = copy
            node = node.next
        
        curr = head
        while curr:
            copy = originalToCopy[curr]
            copy.random = originalToCopy[curr.random]
            copy.next = originalToCopy[curr.next]
            curr = curr.next

        return originalToCopy[head]

