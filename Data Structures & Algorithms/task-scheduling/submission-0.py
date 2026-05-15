import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # First keep track of the frequency of the task
        task_frequency = Counter(tasks)
        # Now, keep the count in a max-heap to know which
        # task has the highest frequency. The highest frequency
        # task must be run first always.
        heap = [-count for count in task_frequency.values()]
        heapq.heapify(heap)
        # Now, we need a queue which will help us
        # keep the tasks which are in cooldown so
        # that we know when a task is ok to pick
        # back and working. For this, we are going
        # to keep the queue have a tuple[int, int]
        # where queue[0][0] is the time we can
        # pick it back again and queue[0][1] is the
        # left frequency of times we need to run
        # this task
        cooldown = deque[tuple[int, int]]()
        time: int = 0
        while heap or cooldown:
            time += 1
            if heap:
                # We have tasks to do.
                # pop a task to work on
                left_count = heapq.heappop(heap) + 1  # Task is consumed
                if left_count < 0:
                    # We still have this task to do. So put the
                    # remaining in cooldown
                    cooldown.append((time + n, left_count))
            if cooldown and cooldown[0][0] == time:
                # We can now release the task in cooldown for execution
                # - so put it back in the heap
                heapq.heappush(heap, cooldown.popleft()[1])
        return time
