# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # global final tracker for ancestor
        # recurse: isAnc(root) -> returns true if it contains p,q including root.
        # isAnc(node) will set anc = node if not set yet
        # return anc

        # REMINDER: set p < q to simply.

        def isAnc(node):
            #base: empty node
            if not node:
                return
            
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            elif p.val < node.val and q.val < node.val:
                return isAnc(node.left)
            elif p.val > node.val and q.val > node.val:
                return isAnc(node.right)
            
        return isAnc(root)

