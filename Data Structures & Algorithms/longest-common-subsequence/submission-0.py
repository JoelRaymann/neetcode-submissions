class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        memory: dict[tuple[int, int], int] = {}

        def _lcs(
            i: int,
            j: int,
        ) -> int:
            if i == n1 or j == n2:
                return 0

            # Check the memory
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup

            # Do the recursive
            result: int = 0
            if text1[i] == text2[j]:
                result = 1 + _lcs(i + 1, j + 1)
            else:
                result = max(_lcs(i + 1, j), _lcs(i, j + 1))
            memory[(i, j)] = result
            return result

        return _lcs(0, 0)