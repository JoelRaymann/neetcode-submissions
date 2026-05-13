import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_inverse = [-stone for stone in stones]
        heapq.heapify(stones_inverse)
        while len(stones_inverse) > 1:
            largest_stone = -heapq.heappop(stones_inverse)
            second_largest_stone = -heapq.heappop(stones_inverse)
            smash_result = abs(largest_stone - second_largest_stone)
            heapq.heappush(stones_inverse, -smash_result)
        return -stones_inverse[0]