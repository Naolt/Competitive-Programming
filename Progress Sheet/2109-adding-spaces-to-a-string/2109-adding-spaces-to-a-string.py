class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        size = len(spaces)
        result = ""
        spaceIndex = 0
        letterIndex = 0
        
        while spaceIndex < size:
            
            if letterIndex == spaces[spaceIndex]:
                result += " "
                spaceIndex += 1
            else:
                result += s[letterIndex]
                letterIndex += 1
                
        if letterIndex <= len(s)-1:
            result += s[letterIndex:]
            
        return result
        