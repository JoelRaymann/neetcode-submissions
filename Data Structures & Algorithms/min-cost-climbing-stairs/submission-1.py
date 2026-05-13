class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory: dict[int, int] = {}
        n = len(cost)

        def _min_cost(i: int) -> int:
            if i >= n:
                return 0
            
            lookup = memory.get(i, None)
            if lookup is not None:
                return lookup
            
            result = cost[i] + min(_min_cost(i + 1), _min_cost(i + 2))
            memory[i] = result
            return result
        
        return min(_min_cost(0), _min_cost(1))