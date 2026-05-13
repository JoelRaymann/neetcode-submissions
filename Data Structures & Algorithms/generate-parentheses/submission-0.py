class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def _generate_parenthesis(
            s: str,
            open: int,
            close: int,
        ) -> None:
            if len(s) == 2 * n:
                results.append(s)
                return None
            # Now, we have 2 options to choose from. When the
            # string has less open than n, we can add "("
            if open < n:
                _generate_parenthesis(s + "(", open + 1, close)
            # If the string "s" has more open than close, we can
            # add the ")" to it.
            if close < open:
                _generate_parenthesis(s + ")", open, close + 1)
            return None

        _generate_parenthesis("", 0, 0)
        return results