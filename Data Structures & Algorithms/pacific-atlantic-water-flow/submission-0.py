class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [
            [-1, 0],
            [1, 0],
            [0, 1],
            [0, -1],
        ]
        # Process ocean nodes
        pacific_ocean_reachable_nodes = set[tuple[int, int]]()
        atlantic_ocean_reachable_nodes = set[tuple[int, int]]()

        def _dfs(node: tuple[int, int], reachable: set[tuple[int, int]]) -> None:
            if node in reachable:
                return None
            reachable.add(node)
            x, y = node
            for move_x, move_y in directions:
                next_x, next_y = x + move_x, y + move_y
                if (
                    (0 <= next_x < rows)
                    and (0 <= next_y < cols)
                    and heights[next_x][next_y] >= heights[x][y]
                ):
                    _dfs((next_x, next_y), reachable)
            return None

        for x in range(rows):
            _dfs((x, 0), pacific_ocean_reachable_nodes)
            _dfs((x, cols - 1), atlantic_ocean_reachable_nodes)

        for y in range(cols):
            _dfs((0, y), pacific_ocean_reachable_nodes)
            _dfs((rows - 1, y), atlantic_ocean_reachable_nodes)

        both_ocean = pacific_ocean_reachable_nodes.intersection(
            atlantic_ocean_reachable_nodes
        )
        return list(both_ocean)