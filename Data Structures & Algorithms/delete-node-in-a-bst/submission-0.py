# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # def _delete_node(
        #     node: TreeNode | None,
        #     key: int,
        # ) -> TreeNode | None:
        # First, Find the node
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # We are at the node to delete
            # CASES:
            # CASE 1: If node is leaf node
            if root.left is None and root.right is None:
                return None
            # CASE 2: There are 2 child nodes
            elif root.left is not None and root.right is not None:
                # Then we need to find the right subtree's smallest value and swap
                # the value with the current node_to_delete value and then rerun
                # delete function.
                successor_node = root.right
                while successor_node.left is not None:
                    successor_node = successor_node.left
                # Now, swap the values
                root.val = successor_node.val
                root.right = self.deleteNode(root.right, successor_node.val)
            # CASE 3: If node has one child. Just swap this node with the child
            else:
                return root.left if root.left is not None else root.right
        return root
    # return _delete_node(root, key)