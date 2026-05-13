class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results, path = [], []

        def _combination_sum(
            index: int,
        ) -> None:
            # The condition for success
            path_sum = sum(path)
            if path_sum == target:
                results.append(path[:])
                return None
            if path_sum > target:
                return None

            # Iterate the choices and work with it.
            for i in range(index, len(nums)):
                # Add the choice
                path.append(nums[i])
                # Explore it. Since, we can choose
                # the same choice unlimited times, we
                # dont move the pointer
                _combination_sum(i)
                # Remove the choice
                path.pop()
            return None

        _combination_sum(0)
        return results