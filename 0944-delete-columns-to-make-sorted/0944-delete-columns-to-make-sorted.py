class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        matchDict = [chr(96)]*len(strs[0])
        deleteCount = 0
        
        for word in strs:
            for index,letter in enumerate(word):
                if letter >= matchDict[index]:
                    matchDict[index] = letter
                else:
                    if matchDict[index] != chr(123):
                        deleteCount += 1
                    matchDict[index] = chr(123)
        
        return deleteCount
    """
    I could have done using column traversing
    space = O(N)
    time = O(N*K)
    """
        