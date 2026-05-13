class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo: dict[int, bool] = {}

        def _word_break(
            start: int,
        ) -> bool:
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set and _word_break(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return _word_break(0)