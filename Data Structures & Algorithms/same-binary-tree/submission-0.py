# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                left_check = self.isSameTree(p.left, q.left)
                right_check = self.isSameTree(p.right, q.right)
                return bool(left_check * right_check)