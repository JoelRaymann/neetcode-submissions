class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memory: dict[tuple[int, int], int] = {}

        def _findTargetSumWays(index: int, sum: int) -> int:
            if index == n:
                if sum == target:
                    return 1
                else:
                    return 0
            lookup = memory.get((index, sum), None)
            if lookup is not None:
                return lookup
            result = _findTargetSumWays(
                index + 1, sum=sum + nums[index]
            ) + _findTargetSumWays(index + 1, sum=sum - nums[index])
            memory[(index, sum)] = result
            return result

        return _findTargetSumWays(1, nums[0]) + _findTargetSumWays(1, -nums[0])