class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map:dict[int, int] = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
            if hash_map[i] > 1:
                return True
            else:
                continue
        return False 