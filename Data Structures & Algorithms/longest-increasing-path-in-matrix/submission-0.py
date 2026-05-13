class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        memory = dict[tuple[int, int], int]()

        def _increasing_path(
            i: int,
            j: int,
        ) -> int:
            lookup: int | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            value = matrix[i][j]
            max_path = 0
            for mx, my in directions:
                nx, ny = i + mx, j + my
                if (0 <= nx < n and 0 <= ny < m) and matrix[nx][ny] > value:
                    max_path = max(max_path, _increasing_path(nx, ny))
            memory[(i, j)] = 1 + max_path
            return 1 + max_path

        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, _increasing_path(i, j))
        return max_path