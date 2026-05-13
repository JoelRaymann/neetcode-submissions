class Solution:
    def rob(self, nums: List[int]) -> int:
        # Define memory
        memory: dict[tuple[int, bool], int] = dict[tuple[int, bool], int]()

        def _rob(
            house_i: int,
            is_first_index_selected: bool = False,
        ) -> int:
            # Base case
            # CASE 1: If we are at the last house, we just have one option,
            # either steal or leave it. We have to leave it if the first house
            # is robbed.
            if house_i == len(nums) - 1:
                if is_first_index_selected is True:
                    return 0
                else:
                    return nums[house_i]
            # CASE 2: If we are at the last - 1 house, we have 2 options,
            # either steal this house, or steal the next house which is the last
            # house.
            if house_i == len(nums) - 2:
                return max(
                    nums[house_i],
                    _rob(house_i + 1, is_first_index_selected),
                )

            # Check memory
            lookup: int | None = memory.get((house_i, is_first_index_selected), None)
            if lookup is not None:
                return lookup
            else:
                pass
            # Recursive case.
            if house_i == 0:
                result = max(
                    nums[house_i] + _rob(house_i + 2, True),
                    _rob(house_i + 1, False),
                )
            else:
                result = max(
                    nums[house_i] + _rob(house_i + 2, is_first_index_selected),
                    _rob(house_i + 1, is_first_index_selected),
                )
            memory[(house_i, is_first_index_selected)] = result
            return result

        return _rob(0)