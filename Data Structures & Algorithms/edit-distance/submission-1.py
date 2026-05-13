class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        memory: dict[tuple[int, int], int] = {}

        def _min_distance(
            i: int,
            j: int,
        ) -> int:
            if j == m:
                # This means we might still have excess letters left in word1. We need delete them
                return n - i
            if i == n:
                # This means we might still have to add letters in word1.
                return m - j
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup

            result = 0
            if word1[i] == word2[j]:
                result = _min_distance(i + 1, j + 1)
            if word1[i] != word2[j]:
                # We have the three possible operations:
                # 1. Replace the character (i + 1, j + 1)
                # 2. Delete the character (i + 1, j)
                # 3. Insert the character before i (i, j + 1)
                result = 1 + min(
                    _min_distance(i + 1, j + 1),
                    _min_distance(i + 1, j),
                    _min_distance(i, j + 1),
                )
            memory[(i, j)] = result
            return result
        return _min_distance(0, 0)