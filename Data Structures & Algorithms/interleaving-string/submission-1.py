class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != n1 + n2:
            return False

        memory: dict[tuple[int, int], bool] = {}

        def _isInterLeave(
            i: int,
            j: int,
        ) -> bool:
            if i == n1 and j == n2:
                return True

            # Memory
            lookup: bool | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            z = i + j
            result: bool = False
            if i < n1 and j < n2 and s1[i] == s2[j] == s3[z]:
                result = _isInterLeave(i + 1, j) or _isInterLeave(i, j + 1)
            elif i < n1 and s1[i] == s3[z]:
                result = _isInterLeave(i + 1, j)
            elif j < n2 and s2[j] == s3[z]:
                result = _isInterLeave(i, j + 1)
            else:
                result = False
            memory[(i, j)] = result
            return result

        return _isInterLeave(0, 0)