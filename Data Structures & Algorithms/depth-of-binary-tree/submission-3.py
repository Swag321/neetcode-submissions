# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque()
        q.append(root)
        depth = 0
        lenQ = len(q)

        while q:
            node = q.popleft()
            lenQ -= 1
            if node:
                q.append(node.left)
                q.append(node.right)
            if lenQ == 0:
                depth += 1
                lenQ = len(q)
        
        return depth - 1