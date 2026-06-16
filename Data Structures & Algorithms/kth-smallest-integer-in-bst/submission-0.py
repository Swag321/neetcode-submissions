# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.num = 0
        self.res = 0

        def dfs(node):

            if not node:
                return
            
            left = dfs(node.left)
            self.num += 1 # leftmost (smallest) element is count 1
            if self.num == k:
                self.res = node.val
            right = dfs(node.right)

        dfs(root)
        return self.res