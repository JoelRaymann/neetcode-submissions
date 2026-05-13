class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memory: Store the results
        memory: dict[int, int] = dict[int, int]()

        def _rob(house_i: int) -> int:
            if house_i >= len(nums):
                return 0

            # Check memory
            lookup: int | None = memory.get(house_i, None)
            if lookup is not None:
                return lookup

            # Calculate results
            result = max(
                nums[house_i] + _rob(house_i + 2),  # Rob the house and go
                _rob(house_i + 1),  # Skip the house and go next
            )
            memory[house_i] = result
            return result

        return _rob(0)