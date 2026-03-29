import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        minHeap = stones
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            diff = x - y
            if not diff:
                continue
            else:
                heapq.heappush(minHeap, diff)
        return -minHeap[0] if minHeap else 0
        