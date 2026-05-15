import heapq
from typing import Self


class KthLargest:

    def __init__(
        self: Self,
        k: int,
        nums: [int],
    ) -> None:
        self.heap = []
        self.k = k
        heapq.heapify(self.heap)
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(
        self: Self,
        val: int,
    ) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
