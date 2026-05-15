import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def _euclidean_distance(
            p1: tuple[int, int],
            p2: tuple[int, int],
        ) -> float:
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        
        heap = []
        for point in points:
            dist = _euclidean_distance(tuple(point), (0, 0))
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]