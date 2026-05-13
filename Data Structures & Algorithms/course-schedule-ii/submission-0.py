class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct the graph here and
        # Construct an hashmap of indegree of nodes
        graph: dict[int, list[int]] = {course: [] for course in range(numCourses)}
        indegree_map: dict[int, int] = {course: 0 for course in range(numCourses)}
        for c1, c2 in prerequisites:
            graph[c2] += [c1]  # C2 -> C1 basically [0, 1] => 1 -> 0 which is what we want.
            indegree_map[c1] += 1

        # now, we need to do BFS from indegree(0) guys
        queue = deque[int]()
        results: list[int] = []
        for node, indegree in indegree_map.items():
            if indegree == 0:
                queue.append(node)
                results.append(node)
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                indegree_map[nei] -= 1
                if indegree_map[nei] == 0:
                    queue.append(nei)
                    results.append(nei)
        return results if len(results) == numCourses else []
