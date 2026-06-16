# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # 1 -> 2,3
        # 

        indices = {val: idx for idx, val in enumerate(inorder)}
        # get {node.val : index} for all values of inorder list

        self.pre_idx = 0
        # start root at index 0 of pre

        def dfs(l,r):
            if l > r:
                # return from recursion stack once we exceed
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1 # incr after setting root val
            
            root = TreeNode(root_val)
            mid = indices[root_val] #index of node in inorder list

            root.left = dfs(l, mid-1) # set left pointer to the left of mid
            root.right = dfs(mid+1,r)

            return root

        return dfs(0, len(inorder)-1)
            


