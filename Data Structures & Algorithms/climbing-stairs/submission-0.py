class Solution:
    def climbStairs(self, n: int) -> int:
        # Define the memory. This will store
        # the results of calculation of previous
        # climb stairs solns.
        memory: dict[int, int] = dict[int, int]()

        def dp(k: int) -> int:
            # Define base case
            if k < 1:
                return 0
            if k == 1:
                return 1
            if k == 2:
                return 2

            # Check memory
            memory_lookup: int | None = memory.get(k, None)
            if memory_lookup is not None:
                return memory_lookup
            else:
                pass

            # Calculate the solution
            result = dp(k - 1) + dp(k - 2)
            # Add it to memory
            memory[k] = result
            return result

        return dp(n)