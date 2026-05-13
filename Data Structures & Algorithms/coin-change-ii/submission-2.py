class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n = len(coins)
        memory: dict[tuple[int, int]] = {}

        def _change(
            remaining: int,
            coin_index: int,
        ) -> int:
            lookup = memory.get((remaining, coin_index), None)
            if lookup is not None:
                return lookup
            total_remaining = remaining - coins[coin_index]
            final = 0
            if total_remaining < 0:
                final = 0
            if total_remaining == 0:
                final = 1
            if total_remaining > 0:
                result = 0
                for index in range(coin_index, n):
                    result += _change(total_remaining, index)
                final = result
            memory[(remaining, coin_index)] = final
            return final

        result = 0
        for index in range(n):
            result += _change(amount, index)
        return result