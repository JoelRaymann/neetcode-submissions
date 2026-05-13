class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        # Digit Mapping
        digit_map: dict[str, list[str]] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        results, path = [], []

        def _combination(
            start: int,
        ) -> None:
            if start == n:
                if len(path) == n:
                    results.append("".join(path[:]))
                return None
            for i in range(start, n):
                # Grab the mapping
                char_list = digit_map.get(digits[i])
                if char_list is None:
                    return None
                for char in char_list:
                    # Add the char to path
                    path.append(char)
                    # Explore the next digit
                    _combination(i + 1)
                    # Pop the char and explore the
                    # next char in the char list
                    path.pop()
            return None

        _combination(0)
        return results