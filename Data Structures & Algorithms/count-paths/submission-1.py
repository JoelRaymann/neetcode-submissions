class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        direction = [
            [1, 0],
            [0, 1],
        ]

        memory: dict[tuple[int, int], int] = {}
        def _dfs(
            i: int,
            j: int,
        ) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if not (0 <= i < m and 0 <=j < n):
                return 0
            
            lookup: int | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            
            result = 0
            for mx, my in direction:
                nx, ny = i + mx, j + my
                result += _dfs(nx, ny)
            memory[(i, j)] = result
            return result
        
        return _dfs(0, 0)