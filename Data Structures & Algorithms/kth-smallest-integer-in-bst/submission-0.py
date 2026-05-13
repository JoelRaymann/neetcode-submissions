# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if root is None:
            raise ValueError("Given tree is empty")
        count: int = 0
        result: int | None = None
        def _kth_smallest(
            node: TreeNode | None,
        ) -> None:
            nonlocal count
            nonlocal result
            if node is None:
                return None
            # Do inorder traveral and keep track of the 
            # nodes
            _kth_smallest(node.left)
            count += 1
            if count == k:
                result = node.val
                return None
            if count > k:
                return None
            _kth_smallest(node.right)
            return None

        _kth_smallest(root)    
        return result
    
    