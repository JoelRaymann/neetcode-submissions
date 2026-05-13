class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            
        n = len(board)
        m = len(board[0])

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        visited = set[tuple[int, int]]()

        def _dfs(
            node: tuple[int, int],
            z: int,
        ) -> bool:
            x, y = node
            if not (0 <= x < n and 0 <= y < m):
                return False

            # Add the node
            visited.add(node)
            if z == len(word) - 1:
                return board[x][y] == word[z]
            # Explore the directions
            if board[x][y] == word[z]:
                result = False
                for mx, my in directions:
                    nx, ny = x + mx, y + my
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                        result = result or _dfs((nx, ny), z + 1)
                visited.discard(node)
                return result
            else:
                # Pop the node
                visited.discard(node)
                return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and _dfs((i, j), 0):
                    return True

        return False