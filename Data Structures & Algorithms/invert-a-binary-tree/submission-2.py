# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = collections.deque()

        q.append(root)

        while q:
            node = q.popleft()

            if node:
                orgL = node.left
                orgR = node.right

                q.append(orgL)
                q.append(orgR)

                node.left = orgR
                node.right = orgL
        
        return root
