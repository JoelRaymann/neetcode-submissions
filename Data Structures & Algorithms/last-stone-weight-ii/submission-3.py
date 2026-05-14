from copy import deepcopy

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        n = len(stones)
        total = sum(stones)
        # We need to minimize (2 * sum(positive choices) - total) => sum(positive_choices) -> total / 2
        target = total // 2

        memory: dict[tuple[int, int], int] = {}
        def _last_stone_weight(
            index: int,
            positive_total: int,
        ) -> int:
            if index == n:
                return abs(2 * positive_total - total)
            
            lookup = memory.get((index, positive_total), None)
            if lookup is not None:
                return lookup

            # Now, we need to choose where to make this
            # stone + or -
            result = min(
                _last_stone_weight(index + 1, positive_total + stones[index]),
                _last_stone_weight(index + 1, positive_total),
            )
            memory[(index, positive_total)] = result
            return result

        return _last_stone_weight(0, 0) 

