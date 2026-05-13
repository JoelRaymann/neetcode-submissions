class Solution:


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
            
        INF = 2**31 - 1
        rows = len(grid)
        cols = len(grid[0])
        queue = deque[tuple[int, int]]([])

        # First, add the treasure points to the queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        direction = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
        ]

        # Now, do BFS on each of these nodes
        while queue:
            node = queue.popleft()
            x, y = node
            for move_x, move_y in direction:
                new_x, new_y = x + move_x, y + move_y
                if (
                    (0 <= new_x < rows)
                    and (0 <= new_y < cols)
                    and grid[new_x][new_y] == INF
                ):
                    grid[new_x][new_y] = 1 + grid[x][y]
                    queue.append((new_x, new_y))

        for i in range(rows):
            for j in range(cols):
                print(grid[i][j])
        return None