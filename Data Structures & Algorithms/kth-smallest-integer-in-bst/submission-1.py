# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        smallCount = 0
        res = 0

        def dfs(node):
            nonlocal smallCount, res
            if not node:
                return

            dfs(node.left)
            if smallCount >= k:
                return
            smallCount += 1
            if smallCount >= k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
