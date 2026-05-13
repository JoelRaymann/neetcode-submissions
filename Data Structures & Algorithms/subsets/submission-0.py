class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        n = len(nums)
        results: list[list[int]] = []

        def _subset(
            index: int,
            array_built: list[int] = [],
        ) -> None:
            if index == n:
                results.append(array_built)
                return None

            # Now, we can either choose this element
            # to be part of the array built or skip
            # this.
            _subset(index + 1, array_built + nums[index : index + 1])
            _subset(index + 1, array_built)
            return None

        _subset(0, [])
        return results