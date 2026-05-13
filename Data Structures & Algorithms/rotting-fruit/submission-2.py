from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque[tuple[int, int]]()

        fresh_fruits = 0
        # Add the rotten apple.
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y))
                elif grid[x][y] == 1:
                    fresh_fruits += 1

        direction = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        # Now, do bfs from the rotten apple while tracking
        # the levels to do so.
        minutes = 0
        while queue and fresh_fruits > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                x, y = node
                for move_x, move_y in direction:
                    next_x, next_y = x + move_x, y + move_y
                    if (
                        (0 <= next_x < rows)
                        and (0 <= next_y < cols)
                        and grid[next_x][next_y] == 1
                    ):
                        grid[next_x][next_y] = 2
                        fresh_fruits -= 1
                        queue.append((next_x, next_y))
            minutes += 1

        return minutes if fresh_fruits == 0 else -1