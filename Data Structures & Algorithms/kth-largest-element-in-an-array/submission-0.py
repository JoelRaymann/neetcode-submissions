import heapq
from copy import deepcopy

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = deepcopy(nums)
        heapq.heapify(nums_heap)
        while len(nums_heap) > k:
            heapq.heappop(nums_heap)
        return nums_heap[0]