class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited: set[tuple[int, int]] = set[tuple[int, int]]()

        def _dfs(
            i_index: int,
            j_index: int,
        ) -> int:
            nonlocal visited
            if not (0 <= i_index < len(grid) and 0 <= j_index < len(grid[0])):
                return 0
            if (i_index, j_index) in visited or grid[i_index][j_index] == 0:
                return 0
            # Add the node to the visited
            visited.add((i_index, j_index))
            # Return the area
            return (
                grid[i_index][j_index]
                + _dfs(i_index + 1, j_index)
                + _dfs(i_index - 1, j_index)
                + _dfs(i_index, j_index + 1)
                + _dfs(i_index, j_index - 1)
            )

        max_area: int = 0
        for i_index in range(len(grid)):
            for j_index in range(len(grid[i_index])):
                if (i_index, j_index) not in visited and grid[i_index][j_index] == 1:
                    max_area = max(max_area, _dfs(i_index, j_index))

        return max_area