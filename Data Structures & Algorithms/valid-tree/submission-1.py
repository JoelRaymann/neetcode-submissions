class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Construct the graph
        graph: dict[int, list[int]] = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]
        print(graph)

        visited = set[int]()

        def _dfs(
            node: int,
            parent_node: int | None = None,
        ) -> bool:
            nonlocal visited
            if node in visited:
                return False
            visited.add(node)
            result = True
            for nei in graph[node]:
                if parent_node is not None and parent_node == nei:
                    continue
                result = result and _dfs(nei, node)
            return result

        return _dfs(0) and len(visited) == n