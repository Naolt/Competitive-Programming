class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        
        for i in arr:
            toBeSearched = i * 2
            if toBeSearched in arr:
                if toBeSearched == 0:
                    if arr.count(toBeSearched) > 1:
                        return True
                else:
                    return True
        return False