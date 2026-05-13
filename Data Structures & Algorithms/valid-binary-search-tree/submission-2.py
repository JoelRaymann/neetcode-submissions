# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _is_valid_bst(
            node: TreeNode | None,
            lower: float,
            upper: float,
        ) -> bool:
            if node is None:
                return True
            if not (lower < node.val < upper):
                return False
            return _is_valid_bst(node.left, lower, node.val) and _is_valid_bst(
                node.right, node.val, upper
            )

        return _is_valid_bst(root, float("-inf"), float("inf"))
