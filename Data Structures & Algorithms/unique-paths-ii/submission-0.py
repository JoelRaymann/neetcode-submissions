class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        direction = [
            [1, 0],
            [0, 1],
        ]

        memory: dict[tuple[int, int], int] = {}

        def _dfs(
            i: int,
            j: int,
        ) -> int:
            
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            lookup: int | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup

            result: int = 0
            for mx, my in direction:
                nx, ny = i + mx, j + my
                result += _dfs(nx, ny)
            memory[(i, j)] = result
            return result
        
        return _dfs(0, 0)