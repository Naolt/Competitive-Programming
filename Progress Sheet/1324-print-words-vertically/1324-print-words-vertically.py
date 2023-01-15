class Solution:
    def printVertically(self, s: str) -> List[str]:
        toList = list(s.split())
        size = len(toList)
        newArr = []
        i = 0
        
        while(True):
            newStr = ""
            for j in range(size):
                if(i < len(toList[j])):
                    newStr +=toList[j][i]
                else:
                    newStr +=" "
            if newStr.rstrip() == "":
                break
            newArr.append(newStr.rstrip())
            i+=1
            
        return newArr