class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:   
        # Think about this way - instead of saying how much coin needed to build something
        # how about amount of coin needed to reduce the total down?
        INF = float("inf")
        memory: dict[int, int] = {}

        def _coin_change(
            remaining: int,
        ) -> int:
            # Base Case
            if remaining == 0:
                return 0
            if remaining < 0:
                # We overshooted, so this is not the right soln tree path
                return INF

            # Check memory
            lookup: int | None = memory.get(remaining, None)
            if lookup is not None:
                return lookup

            # Recursive case. 1 (current depth) + min depth of paths which will make it go down to 0.
            best_result = INF
            for coin in coins:
                soln = 1 + _coin_change(remaining - coin)
                best_result = min(best_result, soln)
            memory[remaining] = best_result
            return best_result

        result = _coin_change(amount)
        return -1 if result == INF else result