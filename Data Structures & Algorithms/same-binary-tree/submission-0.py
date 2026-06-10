# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recurse on dfs(pchild, qchild): if pchild.val != qchild.val return false

        def dfs(pc, qc) -> bool:
            if not pc and not qc:
                return True #both none
            elif not pc or not qc:
                return False # either one is None but not both
            elif pc.val == qc.val:
                cl = dfs(pc.left, qc.left)
                cr = dfs(pc.right, qc.right)
                return cl and cr # False if either left or right child is not same
            else:
                return False
        
        return dfs(p, q)