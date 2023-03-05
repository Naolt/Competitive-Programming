class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        newTickets = [[i,x] for i,x in enumerate(tickets)]
        queue = deque(newTickets)
        count = 1     
        while queue:
            front = queue.popleft()
            front[1] -= 1
            if front[1] > 0:
                queue.append(front)
            else:
                if front[0] == k:
                    break
            count += 1
        return count