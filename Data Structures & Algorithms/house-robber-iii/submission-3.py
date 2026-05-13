# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # At any instance, we have an option to
        # either rob this house - skipping the childrens
        # or skip this, allowing us to rob the child of this
        # root.
        def _dfs(
            node: TreeNode | None,
        ) -> tuple[int, int]:
            # At each instance, we are going to give 2 values
            # value if we robbed this place and value if we
            # skipped this place.
            if node is None:
                return (0, 0)
            # Now, lets compute the left side and right side
            left_rob, left_skip = _dfs(node.left)
            right_rob, right_skip = _dfs(node.right)
            # Now, if I rob the house, I will be skipping
            # the children. The value for that computation
            # is given by left_skip and right_skip as they
            # provide me what happens when I skip them.
            rob_value = node.val + left_skip + right_skip
            # Now, if I skip this house, then I will either
            # rob my children or skip them. That value is provided
            # to us. We need to just take the max outcome option
            rob_skip = max(left_rob, left_skip) + max(right_rob, right_skip)
            # Now, lets just return these values down
            return rob_value, rob_skip
        
        return max(_dfs(root))
