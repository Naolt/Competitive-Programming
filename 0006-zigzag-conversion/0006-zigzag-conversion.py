class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strList = []
        
        counter = 0
        size = len(s)
        
        flag = False
        result = ""
        

        while counter < size:
            text = ""
            if not flag:
                for i in range(numRows):
                    text += s[counter]
                    counter += 1
                    if counter >= size:
                        break
                flag = True
                strList.append(text)
                
                    
            else:
                for i in range(numRows-2):
                    text += s[counter]
                    counter += 1
                    if counter >= size:
                        j = i
                        print("here")
                        if j < numRows-2:
                            while(j < numRows-3):
                                text +=" "
                                j+=1      
                        break
                flag = False
                strList.append((" "+text+" ")[::-1])
        
        listSize = len(strList)
                
        for i in range(numRows):
            
            for j in range(listSize):
               
                if  i < len(strList[j]) and strList[j][i] != " ": 
                    result += strList[j][i]
        return result