class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        memory: dict[tuple[int, int], bool] = {}

        def _regex_match(
            i: int,
            j: int,
        ) -> bool:
            # Base case - if the pattern is consumed
            if j == m:
                # Check if string "s" is also consumed
                return i == n

            # Lookup
            lookup: bool | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup

            # Now lets do the match.
            # This is the condition to consume a character
            first_match = i < n and (s[i] == p[j] or p[j] == ".")

            if j + 1 < m and p[j + 1] == "*":
                # This means we have options now. We either use
                # 0 copies of p[j] or consume a copy of p[j]
                # Consume s[i] or skip p[j]
                result = (first_match and _regex_match(i + 1, j)) or _regex_match(
                    i, j + 2
                )  # Why? We are skippign p[j]* together.
                # NOTE: * => zero or many occurence of p[j] so we can skip p[j] altogether.
            else:
                result = first_match and _regex_match(i + 1, j + 1)
            memory[(i, j)] = result
            return result

        return _regex_match(0, 0)