# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recurse down to end layer, invertingTree each time
        # what is end layer?: if root is None.
        # cases: root.left is none or root.right is none? its ok just swap them.


        if not root:
            return
        
        self.invertTree(root.left) #leftmost: 4's left,right return none; 4 swaps l,r and returns; 2 swaps 4,5 returns...
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root