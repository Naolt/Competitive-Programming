class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:        
        valDict = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                valDict[bill] += 1
            elif bill == 10:
                if valDict[5] == 0:
                    return False
                valDict[5] -= 1
                valDict[10] += 1
            else:
                if valDict[5] == 0:
                    return False
                elif valDict[10] > 0:
                    valDict[10] -= 1
                    valDict[5] -= 1
                else:
                    if valDict[5] < 3:
                        return False
                    valDict[5] -= 3
        
        
        return True