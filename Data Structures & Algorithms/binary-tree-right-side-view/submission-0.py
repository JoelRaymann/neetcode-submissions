# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        bfs_queue: list[TreeNode] = deque[TreeNode]([root])
        level: int = 1
        next_level: int = 0
        results: list[int] = []
        while bfs_queue:
            current_node = bfs_queue.popleft()
            if current_node.left is not None:
                bfs_queue.append(current_node.left)
                next_level += 1
            if current_node.right is not None:
                bfs_queue.append(current_node.right)
                next_level += 1
            level -= 1
            if level == 0:
                results.append(current_node.val)
                level = next_level
                next_level = 0

        return results