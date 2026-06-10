# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # approach: get depth for each node, {d1: [1], d2:[2,3]}
        # time: O(n) to get depth of all rows + O(h) = O(n)
        # space: O(h + n) = O(n) worst case all nodes in one level or if perfectly skewed

        # approach 2: bfs. queue = [(0,1), (1,2), (1,3), ... (parentLevel+1, child)]
        # as item = queue.popleft() -> append item[1] to result at index item[0]
        # return result
        # time: O(n). Space: O(n)

        i = 0 #queue start position
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        
        return res
            



