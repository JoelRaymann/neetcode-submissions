# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total_good_nodes = 0

        def _good_nodes(
            node: TreeNode | None,
            max_value: int
        ) -> None:
            nonlocal total_good_nodes
            if node is None:
                return None

            if node.val >= max_value:
                max_value = node.val
                total_good_nodes += 1
            # Traverse
            _good_nodes(node.left, max_value=max_value)
            _good_nodes(node.right, max_value=max_value)
            return None

        _good_nodes(root, root.val)
        return total_good_nodes