# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # for each node in root, check if tree == subroot
        # O(m*n) time and O(m+n) space (space how?)

        if not subRoot:
            return True

        def sameTree(org,sub) -> bool:
            """
            base case: 
            if sub == null: true
            if org == null: False since sub is not null

            if p == q: recurse
            else: return False
            """
            if not sub and not org:
                return True # both end
            elif not sub or not org:
                return False # one ended earlier.
            # question: what if main ended but subroot still had more?
            
            if org.val == sub.val:
                return sameTree(org.left, sub.left) and sameTree(org.right, sub.right)
            else:
                return False
        
        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True

            return dfs(node.left) or dfs(node.right)
            
            # return False #if unable to find
            
        return dfs(root)
            

