class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memory: dict[int, int] = {}

        def _LIS(
            start: int,
        ) -> int:
            nonlocal memory
            if start >= n:
                return 0
            
            lookup = memory.get(start, None)
            if lookup is not None:
                return lookup
            
            result = 1
            for i in range(start + 1, n):
                if nums[i] > nums[start]:
                    result = max(
                        result,
                        1 + _LIS(i),
                        _LIS(i)
                    )
            memory[start] = result
            return result
        return max(_LIS(i) for i in range(n))