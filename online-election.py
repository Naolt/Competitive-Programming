class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = []
        numDict = defaultdict(int)
        currentMax = persons[0]
        for num in persons:
            numDict[num] += 1
            if numDict[num] > numDict[currentMax]:
                self.persons.append((num,numDict[num],num))
                currentMax = num
            elif numDict[num] == numDict[currentMax]:
                self.persons.append((num,numDict[num],num))
                currentMax = num
            else:
                self.persons.append((num,numDict[num],currentMax))
        print(self.persons)

    def q(self, t: int) -> int:
        left = -1
        right = len(self.times)

        while left+1<right:
            middle = left +(right-left)//2

            if self.times[middle] < t:
                left = middle
            else:
                right = middle
        print("time",t,self.persons[left],left)
        if left+1 >= len(self.persons) or self.times[left+1] != t:
            if left+1 >= len(self.persons):
                return self.persons[-1][2]
            return self.persons[left][2]
        else:
            return self.persons[left+1][2]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)