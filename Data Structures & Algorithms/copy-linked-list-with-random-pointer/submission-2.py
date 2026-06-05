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
        # one pass with defaultdict

        oldToCopy = defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        node = head
        while node:
            copy = oldToCopy[node]
            copy.val = node.val
            copy.next = oldToCopy[node.next]
            copy.random = oldToCopy[node.random]
            node = node.next

        return oldToCopy[head]
        