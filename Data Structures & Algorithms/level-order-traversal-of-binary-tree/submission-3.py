# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        results: list[list[int]] = []
        queue = deque[TreeNode]([root])
        nodes_in_this_level = 1
        nodes_in_next_level = 0
        intermediate_result: list[int] = []
        while queue:
            node = queue.popleft()
            intermediate_result.append(node.val)
            nodes_in_this_level -= 1
            if node.left is not None:
                queue.append(node.left)
                nodes_in_next_level += 1
            if node.right is not None:
                queue.append(node.right)
                nodes_in_next_level += 1
            if nodes_in_this_level == 0:
                results.append(intermediate_result)
                intermediate_result = []
                nodes_in_this_level = nodes_in_next_level
                nodes_in_next_level = 0
        return results