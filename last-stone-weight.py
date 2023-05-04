class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-1*stone)
        while len(heap) > 1:
            largest = heapq.heappop(heap)
            secondLargest = heapq.heappop(heap)
            heapq.heappush(heap,largest-secondLargest)
        return 0 if not heap else -1*heap[-1]