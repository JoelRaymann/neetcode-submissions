class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memory: dict[tuple[int, int], int] = {} 
        def advantage(
            i: int,
            j: int,
        ) -> int:
            if i > j:
                return 0
            if i == j:
                return piles[i]
            
            lookup: int | None = memory.get((i, j), None)
            if lookup is not None:
                return lookup
            
            result = max(
                piles[i] - advantage(i + 1, j),
                piles[j] - advantage(i, j - 1),
            )
            memory[(i, j)] = result
            return result
        return advantage(0, len(piles) - 1) > 0