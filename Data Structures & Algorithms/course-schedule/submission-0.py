class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construct the graph
        graph: dict[int, list[int]] = {course: [] for course in range(numCourses)}
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        # Now, do dfs and keep 2 sets, one is visiting and one is done.
        visiting = set[int]()
        done = set[int]()

        def _dfs(
            node: int,
        ) -> bool:
            nonlocal visiting
            nonlocal done
            if node in visiting:
                return False
            if node in done:
                return True

            visiting.add(node)

            for nei in graph[node]:
                if not _dfs(nei):
                    return False

            # The node is confirmed not having any cycle. We
            # can remove this from visiting and move it to done.
            visiting.remove(node)
            done.add(node)

            return True

        for node in graph.keys():
            if not _dfs(node):
                return False
        return True
