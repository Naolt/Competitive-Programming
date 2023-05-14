class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles[:] = map(lambda x:-1*x,piles)
        heapq.heapify(piles)
        for i in range(k):
            biggest = heapq.heappop(piles)
            heapq.heappush(piles,biggest-(-1*((-1*biggest)//2)))

        return -1*sum(piles)