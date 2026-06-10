# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameterOfRoot = recurse(root.left) + recurse(root.right)
        # return max(diameterOfRoot + 1, depth(root) + 1)

        self.longest = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            height = max(left,right) + 1
            self.longest = max(self.longest, left+right)

            return height
        
        dfs(root)
        return self.longest