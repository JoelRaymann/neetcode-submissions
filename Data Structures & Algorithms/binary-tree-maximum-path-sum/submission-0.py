# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            raise ValueError(f"Given root is empty")
        max_path_sum: int = root.val

        def _max_path_sum(
            node: TreeNode | None,
        ) -> int:
            nonlocal max_path_sum
            if node is None:
                return 0
            result = node.val
            left_max = max(
                _max_path_sum(node.left), 0
            )  # Why? Simple, we don't want any negative paths at all as it is useless
            right_max = max(
                _max_path_sum(node.right), 0
            )  # Same for right side. Whats the point of including a subtree that results in negative final value.

            # Total path cost is result + left side max path + right side max path.
            max_path_sum = max(result + left_max + right_max, max_path_sum)

            return max(
                result,
                result + max(left_max, right_max),
            )  # Either just send the node data or the node data + whichever path
            # gives max value. We need to only send the max thou - that decides which path makes sense - just the root alone or a root
            # with a child tree included.

        _max_path_sum(root)
        return max_path_sum