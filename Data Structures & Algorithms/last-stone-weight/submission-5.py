import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            diff = x - y
            if not diff:
                continue
            else:
                heapq.heappush(maxHeap, diff)
        return -maxHeap[0] if maxHeap else 0
        