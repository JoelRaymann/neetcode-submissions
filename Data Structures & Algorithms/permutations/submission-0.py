class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        result = []
        state = []
        selected: list[bool] = [False] * n

        def _permute() -> None:
            if len(state) == n:
                result.append(state[:])
                return None

            # Go through all choices
            for index, value in enumerate(nums):
                if selected[index] is False:
                    # Make the choice to select this
                    selected[index] = True
                    state.append(value)
                    # Explore the rest
                    _permute()
                    # Backtrack
                    selected[index] = False
                    state.pop()
            return None

        _permute()
        return result
