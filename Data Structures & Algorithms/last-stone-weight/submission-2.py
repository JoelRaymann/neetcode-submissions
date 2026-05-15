import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while heap:
            if len(heap) == 1:
                return -heap[0]
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            z = abs(x - y)
            heapq.heappush(heap, -z)
        return 0