# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(lower, node, upper):
            if not node:
                return True
            mVal = node.val
            lVal = node.left.val if node.left else float('-inf')
            rVal = node.right.val if node.right else float('inf')

            if not lVal < mVal < rVal:
                return False
            
            if not lower < mVal < upper:
                return False

            return dfs(lower, node.left, node.val) and dfs(node.val, node.right, upper)
        
        return dfs(float("-inf"), root, float("inf"))

