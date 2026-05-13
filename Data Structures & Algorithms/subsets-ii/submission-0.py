class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result, path = [], []

        def _subsets_deduped(
            index: int,
        ) -> None:
            result.append(path[:])
            for i in range(index, n):
                # avoid picking the same element path again.
                if i > index and nums[i] == nums[i - 1]:
                    continue
                # pick the choice
                path.append(nums[i])
                # Explore
                _subsets_deduped(i + 1)
                # Backtrack the path
                path.pop()

        nums.sort()
        _subsets_deduped(0)
        return result