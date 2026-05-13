class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memory: dict[tuple[int, int], int] = {}

        def _max_coins(
            i: int,
            j: int,
        ) -> int:
            if j - i < 2:
                return 0

            # Check memory
            lookup = memory.get((i, j), None)
            if lookup is not None:
                return lookup

            result = 0
            for k in range(i + 1, j):
                result = max(
                    result,
                    nums[i] * nums[k] * nums[j] + _max_coins(i, k) + _max_coins(k, j),
                )
            memory[(i, j)] = result
            return result

        nums = [1] + nums + [1]
        return _max_coins(0, len(nums) - 1)