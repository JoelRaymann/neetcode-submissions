class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
                return 0
        # Add in the beginWord if not there
        if beginWord not in wordList:
            words = wordList + [beginWord]
        else:
            words = wordList

        # build the graph
        graph: dict[str, list[str]] = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                graph[pattern].append(word)

        # BFS
        queue = deque[tuple[str, int]]([(beginWord, 1)])
        visited = set[str](beginWord)

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]

                for nei in graph[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, distance + 1))
        return 0