# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEqualTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None or q is None:
            return p is q
        else:
            if p.val != q.val:
                return False
            else:
                return self.isEqualTree(p.left, q.left) and self.isEqualTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isEqualTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
