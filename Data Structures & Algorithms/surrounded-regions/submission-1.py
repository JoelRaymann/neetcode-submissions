class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set[tuple[int, int]]()
        nodes_to_update = set[tuple[int, int]]()

        direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        def _dfs(
            node: tuple[int, int],
        ) -> bool:
            nonlocal visited
            nonlocal nodes_to_update
            x, y = node
            if not (0 <= x < rows and 0 <= y < cols):
                return False
            if node in visited or board[x][y] == "X":
                return True
            visited.add(node)
            nodes_to_update.add(node)
            result = True
            for mx, my in direction:
                nx, ny = x + mx, y + my
                result = result * _dfs((nx, ny))
            return result

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O" and (x, y) not in visited:
                    nodes_to_update = set[tuple[int, int]]()
                    result = _dfs((x, y))
                    if result:
                        for node in nodes_to_update:
                            board[node[0]][node[1]] = "X"

        return None