class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sub = []

        for index,[cityA,cityB] in enumerate(costs):
            sub.append((cityA-cityB,index))
        sub.sort()

        total = 0
        size = len(costs)
        for i, (_ ,index) in enumerate(sub):
            if i < size//2:
                total += costs[index][0]
            else:
                total += costs[index][1]

        return total