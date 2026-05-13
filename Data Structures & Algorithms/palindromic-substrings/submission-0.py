class Solution:
    def countSubstrings(self, s: str) -> int:
        # The idea is that we expand both right and left and check if
        # they are a palindrome by checking char[left] == char[right]

        count: int = 0

        def _extend(left: int, right: int) -> None:
            nonlocal count
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return None
            count += 1
            _extend(left - 1, right + 1)

        for index in range(len(s)):
            # odd ones
            _extend(index, index)
            # even ones
            _extend(index, index + 1)

        return count