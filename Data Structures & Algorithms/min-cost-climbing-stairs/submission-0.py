class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memory. Store the hash of the cost with the result
        memory: dict[int, int] = dict[int, int]()

        def dp(k: list[int]) -> int:
            # Base Case
            k_len = len(k)
            if k_len <= 1:  # Fpr 1 element, you can just directly take 2 step
                # and reach the top
                return 0
            if k_len == 2:
                return min(k)

            # Check memory
            k_hash = hash(tuple(k))
            lookup: int | None = memory.get(k_hash, None)
            if lookup is not None:
                return lookup

            # Recursive case
            result = min(
                k[0] + dp(k[1:]),
                k[1] + dp(k[2:]),
            )
            memory[k_hash] = result
            return result

        return dp(cost)