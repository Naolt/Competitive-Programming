class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        endDic = defaultdict(int)
        for row in wall:
            last = 0
            for cell in row:
                endDic[last+cell] += 1
                last += cell
        del endDic[sum(wall[0])]
        return len(wall) if not endDic else len(wall)-max(list(endDic.values()))

        