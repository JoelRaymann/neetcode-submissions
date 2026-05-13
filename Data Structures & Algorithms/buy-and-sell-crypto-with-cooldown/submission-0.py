class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Memory
        memory: dict[tuple[int, int], int] = {}

        def _max_profit(
            i: int,
            bought_price: int,
        ) -> int:
            if i >= n:
                return 0

            # Check the memory
            lookup = memory.get((i, bought_price), None)
            if lookup is not None:
                return lookup

            # Actions we can do when we have the coin
            result = 0
            if bought_price != -1:
                if bought_price <= prices[i]:
                    # We can sell it right now or hold it.
                    profit = prices[i] - bought_price
                    result = max(
                        profit + _max_profit(i + 2, -1),
                        _max_profit(i + 1, bought_price),
                    )
                else:
                    # Whats the point of selling now? Buy high sell low huh?
                    result = _max_profit(i + 1, bought_price)
            else:
                # We can choose to buy now or skip
                result = max(
                    _max_profit(i + 1, prices[i]),
                    _max_profit(i + 1, -1),
                )
            memory[(i, bought_price)] = result
            return result

        return _max_profit(0, -1)
