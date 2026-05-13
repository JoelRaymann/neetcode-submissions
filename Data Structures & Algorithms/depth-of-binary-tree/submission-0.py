# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if root is None:
            return depth
        depth += 1
        left_depth = self.maxDepth(root.left, depth)
        right_depth = self.maxDepth(root.right, depth)
        return max(depth, left_depth, right_depth)
