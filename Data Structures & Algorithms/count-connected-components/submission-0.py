class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Make the graph
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]

        visited = set[int]()

        def _dfs(
            node: int,
        ) -> None:
            nonlocal visited
            if node in visited:
                return None
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    _dfs(nei)
            return None

        result = 0
        for node in graph.keys():
            if node not in visited:
                result += 1
                _dfs(node)
            else:
                pass
        return result