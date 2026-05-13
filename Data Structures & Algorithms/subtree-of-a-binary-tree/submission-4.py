# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Self


class Solution:
    def isEqualTree(
        self: Self,
        root1: TreeNode | None,
        root2: TreeNode | None,
    ) -> bool:
        if root1 is None or root2 is None:
            return root1 is root2
        else:
            return (
                root1.val == root2.val
                and self.isEqualTree(root1.left, root2.left)
                and self.isEqualTree(root1.right, root2.right)
            )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True

        if root is None:
            return False

        if root.val == subRoot.val and self.isEqualTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
