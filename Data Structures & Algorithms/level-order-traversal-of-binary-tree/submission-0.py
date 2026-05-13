# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        compiled_result: list[list[int]] = []
        bfs_queue = deque[list[TreeNode]]([[root]])
        while bfs_queue:
            level_nodes: list[TreeNode] = bfs_queue.popleft()
            next_level_nodes: list[TreeNode] = []
            result: list[int] = []
            for node in level_nodes:
                result.append(node.val)
                if node.left is not None:
                    next_level_nodes.append(node.left)
                if node.right is not None:
                    next_level_nodes.append(node.right)
            compiled_result.append(result)
            if next_level_nodes:
                bfs_queue.append(next_level_nodes)
        return compiled_result