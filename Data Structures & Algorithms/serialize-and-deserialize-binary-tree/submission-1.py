# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Self


class Codec:
    
    def serialize(
        self: Self,
        root: TreeNode | None,
    ) -> str:
        if root is None:
            return ""
        # We can simply do bfs traversal and construct a string accordingly.
        result: str = ""
        bfs_queue = deque[TreeNode]([root])
        result += f"{root.val},"
        while bfs_queue:
            node = bfs_queue.popleft()
            if node.left is not None:
                result += f"{node.left.val},"
                bfs_queue.append(node.left)
            else:
                result += f"N,"
            if node.right is not None:
                result += f"{node.right.val},"
                bfs_queue.append(node.right)
            else:
                result += f"N,"
            
        print(result)
        return result

    def deserialize(
        self: Self,
        data: str,
    ) -> TreeNode | None:
        if not data:
            return None
        bfs_queue = deque[TreeNode]()
        data_split = data.split(",")
        root = TreeNode(int(data_split[0]))
        bfs_queue.append(root)
        index = 1
        while bfs_queue and index < len(data_split):
            node = bfs_queue.popleft()

            # Left child of the node
            string_val_left = data_split[index]
            if string_val_left == "N":
                node.left = None
            else:
                node.left = TreeNode(int(string_val_left))
                bfs_queue.append(node.left)
            index += 1

            # Right child of the node
            string_val_right = data_split[index]
            if string_val_right == "N":
                node.right = None
            else:
                node.right = TreeNode(int(string_val_right))
                bfs_queue.append(node.right)
            index += 1

        return root
