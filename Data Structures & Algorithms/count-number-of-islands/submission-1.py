class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            islands = 0
            visited: set[tuple[int, int]] = set()
            grid_n = len(grid)
            grid_m = len(grid[0])

            def dfs(
                i: int,
                j: int,
            ) -> None:
                # Traversal routes
                traversal = [
                    (i - 1, j),  # Moving up
                    (i, j - 1),  # Moving left
                    (i + 1, j),  # Moving down
                    (i, j + 1),  # Moving right
                ]
                for move_i, move_j in traversal:
                    if (
                        (move_i, move_j) not in visited
                        and 0 <= move_i < grid_n
                        and 0 <= move_j < grid_m
                        and grid[move_i][move_j] == "1"
                    ):
                        visited.add((move_i, move_j))
                        dfs(move_i, move_j)
                    else:
                        visited.add((move_i, move_j))
                return None

            for row in range(grid_n):
                for col in range(grid_m):
                    if (row, col) in visited:
                        continue
                    else:
                        visited.add((row, col))
                    if grid[row][col] == "1":
                        islands += 1
                        # Explore and find the entire island
                        dfs(row, col)
                    else:
                        pass
            return islands