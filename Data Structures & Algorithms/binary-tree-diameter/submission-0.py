# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter: int = 0

        def height(node: Node | None):
            nonlocal diameter
            if node is None:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)

            # Update the diameter
            diameter = max(diameter, left_h + right_h)
            # Return the height of the parent
            return 1 + max(left_h, right_h)

        height(root)
        return diameter