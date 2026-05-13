class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited: set[tuple[int, int]] = set[tuple[int, int]]()

        def _dfs(
            i_index: int,
            j_index: int,
        ) -> None:
            nonlocal visited
            if not (0 <= i_index < len(grid) and 0 <= j_index < len(grid[0])):
                return None
            if (i_index, j_index) in visited or grid[i_index][j_index] == "0":
                return None

            visited.add((i_index, j_index))
            # Explore nearby
            _dfs(i_index + 1, j_index)
            _dfs(i_index - 1, j_index)
            _dfs(i_index, j_index + 1)
            _dfs(i_index, j_index - 1)
            return None

        total_islands: int = 0
        for i_index in range(len(grid)):
            for j_index in range(len(grid[i_index])):
                if grid[i_index][j_index] == "1" and (i_index, j_index) not in visited:
                    total_islands += 1
                    _dfs(i_index, j_index)
                else:
                    pass

        return total_islands