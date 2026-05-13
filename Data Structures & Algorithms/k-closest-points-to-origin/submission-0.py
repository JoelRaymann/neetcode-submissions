import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt(abs(point[0] ** 2 + point[1] ** 2)), point) for point in points]
        heapq.heapify(heap)
        results: list[list[int]] = []
        for _ in range(k):
            if heap:
                dist, point = heapq.heappop(heap)
                results.append(point)
            else:
                break
        return results