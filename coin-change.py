class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.getChange(coins,amount,0,{0:0})
      

    def getChange(self,coins,amount,count,memo):

        queue = deque([0])
        count = 0
        visited = set([0])
        while queue:
            size = len(queue)
            for i in range(size):
                last = queue.popleft()
                if last == amount:
                    return count
                for coin in coins:
                    if last + coin <= amount and last + coin not in visited:
                        queue.append(last+coin)
                        visited.add(last+coin)
            count += 1
        return -1