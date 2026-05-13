class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False 
        value_to_match = sum(nums) / 2

        def _partition(
            index: int,
            remaining: int,
        ) -> bool:
            if index == n:
                return False
            if remaining == 0:
                return True
            if remaining < 0:
                return False
            return _partition(index + 1, remaining - nums[index]) or _partition(index + 1, remaining)
        
        return _partition(0, value_to_match)