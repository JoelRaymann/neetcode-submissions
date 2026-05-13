class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [
            [1, 0],  # Move down
            [0, 1],  # Move right
        ]
        memory: dict[tuple[int, int], int] = {}

        def _dfs(
            node: tuple[int, int],
        ) -> int:
            nonlocal memory
            if node in memory.keys():
                return memory[node]
            x, y = node
            if not (0 <= x < m and 0 <= y < n):
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            memory[node] = 0
            for mx, my in directions:
                nx, ny = x + mx, y + my
                if (nx, ny) not in memory.keys():
                    memory[node] += _dfs((nx, ny))
                else:
                    memory[node] += memory[(nx, ny)]
            return memory[node]

        return _dfs((0, 0))