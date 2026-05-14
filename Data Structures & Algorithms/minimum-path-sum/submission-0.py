class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        direction = [
            [1, 0],
            [0, 1],
        ]
        
        memory: dict[tuple[int, int], int] = {}

        INF = float('inf')

        def _dfs(
            i: int,
            j: int,
        ) -> int:
            if not (0 <= i < n and 0 <= j < m):
                return INF
            
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            result: int = INF
            for mx, my in direction:
                nx, ny = i + mx, j + my
                result = min(
                    result,
                    _dfs(nx, ny),
                )
            if result == INF:
                memory[(i, j)] = grid[i][j]
                return grid[i][j]
            else:
                memory[(i, j)] = grid[i][j] + result
                return result + grid[i][j]

        return _dfs(0, 0)