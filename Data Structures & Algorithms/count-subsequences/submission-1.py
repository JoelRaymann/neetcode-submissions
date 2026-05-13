class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        memory: dict[tuple[int, int], int] = {}

        def _num_distinct(
            i: int,
            j: int,
        ) -> int:
            if j == m:
                return 1
            if i == n:
                return 0
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            if s[i] == t[j]:
                result = _num_distinct(i + 1, j) + _num_distinct(i + 1, j + 1)
            else:
                result = _num_distinct(i + 1, j)
            memory[(i, j)] = result
            return result

        return _num_distinct(0, 0)
