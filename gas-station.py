class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total,start = 0,0


        for i in range(len(gas)):
            total += gas[i]-cost[i]

            if total < 0:
                total = 0
                start = i+1
            

        return -1 if sum(gas) < sum(cost) else start