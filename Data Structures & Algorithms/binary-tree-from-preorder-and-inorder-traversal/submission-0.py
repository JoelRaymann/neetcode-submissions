# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map_inorder = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def _build_tree(
            left: int,
            right: int,
        ) -> TreeNode | None:

            nonlocal preorder_index

            # If left > right, we have no element in this subtree - its joever here.
            if left > right:
                return None

            # Get the element
            root_element = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(root_element)

            # Split the inorder into left and right subtree
            mid = hash_map_inorder[root_element]

            # Left tree building
            node.left = _build_tree(left=left, right=mid - 1)
            # Right tree building
            node.right = _build_tree(left=mid + 1, right=right)
            # Return the node
            return node

        return _build_tree(0, len(inorder) - 1)