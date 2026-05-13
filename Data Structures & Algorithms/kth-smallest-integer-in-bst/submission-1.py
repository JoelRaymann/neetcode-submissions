# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This is just inorder traversal
        count = 0
        result: int = root.val
        def _kth_smallest(
            node: Node | None,
        ) -> None:
            nonlocal count
            nonlocal result
            if node is None:
                return None
            _kth_smallest(node.left)
            count += 1
            if count == k:
                result = node.val
                return None
            _kth_smallest(node.right)
            return None
            
        _kth_smallest(root)
        return result