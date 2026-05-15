class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memory: dict[int, int] = {}
        def _sum(
            remaining: int,
        ) -> int:
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            lookup = memory.get(remaining, None)
            if lookup is not None:
                return lookup
            
            result = 0
            for num in nums:
                result += _sum(remaining - num)
            memory[remaining] = result
            return result

        
        return _sum(target)