class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque([[0,0]])
        prefix,res= 0,float('inf')
        for index,num in enumerate(nums):
            prefix += num
            while len(queue) > 0 and queue[-1][0] > prefix:
                queue.pop()
            while queue and prefix-queue[0][0] >= k:
                res = min(res,index+1 - queue.popleft()[1])
            queue.append([prefix,index+1])
        return res if res < 10**9 else -1