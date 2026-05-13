class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        memory: dict[tuple[int, int], int] = {}

        def _lcs(
            i: int,
            j: int,
        ) -> int:

            if i == n or j == m:
                return 0
            
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            
            if text1[i] == text2[j]:
                # We move the pointer for both side
                result = 1 + _lcs(i + 1, j + 1)
            else:
                result = max(
                    _lcs(i + 1, j), # We need to explore either moving pointer on left
                    _lcs(i, j + 1), # or pointer on the right.
                )
            memory[(i, j)] = result
            return result
        
        return _lcs(0, 0)