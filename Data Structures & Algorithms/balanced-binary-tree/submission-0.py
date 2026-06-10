# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recurse on each node's chilren.
        # each child returns: "balanced", "unbalanced", "barelyBalanced"

        # balance = ["balanced", "unbalanced", "barelyBalanced"]

        # def dfs (node) -> str:
        #     if not node:
        #         return balance[0]

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if left == balance[1] or right == balance[1]:
        #         return balance[1]
            
        #     if left == balance[2] and not node.right:
        #         return balance[1]

        #     if right == balance[2] and not node.left:
        #         return balance[1]
            
        #     if left == balance[2] and right == balance[2]:
        #         return balance[1]
            
        #     if left == balance[0] and right == balance[0]:
        #         return balance[0]
            
        # output = dfs(root)
        # return True if output in ["balanced", "barelyBalanced"] else False
            
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1  # propagate unbalanced up
            if abs(left - right) > 1:
                return -1  # unbalanced at this node

            return max(left, right) + 1  # return height

        return dfs(root) != -1
