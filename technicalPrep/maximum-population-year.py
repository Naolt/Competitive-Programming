class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0]*2051


        for birth,death in logs:
            prefix[birth] += 1
            prefix[death] -= 1

        prefix = list(accumulate(prefix))
        maxYear = 0

        for index,curr in enumerate(prefix):
            if prefix[maxYear] < curr:
                maxYear = index

        return maxYear