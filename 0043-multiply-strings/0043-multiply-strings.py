"""

num1 = "123", num2 = "456"
            
    3*1 =3+2*10+1*100

approach:
- create dictrionary to encode numbers 0 to 9
- start from the back of the word and iterate by multiplying by base 10 starting from 1




"""

class Solution:
    
    def toNumber(self,num) -> int:
        size = len(num)
        numDict = {}
        for i in range(10):
            numDict[str(i)] = i
        
        i = 1
        result = 0
        while len(str(i)) <= len(num):
            result += numDict[num[size-len(str(i))]] * i
            print(numDict[num[size-len(str(i))]])
            i *= 10
        
        return result    
        
        
        
        
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.toNumber(num1) * self.toNumber(num2))
        