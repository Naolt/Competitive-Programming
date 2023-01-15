"""
["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   
  i
                                             
multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    
"""
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = ""
        size = len(source)
        dontAppend = False
        dontAppend2 = False
        notAllowed = {'/':1,}
        
        for lineIndex in range(size):
            line = source[lineIndex]
            lineSize = len(line)
            # print(line)
            letterIndex = 0
            singleFound = False
            if lineSize == 1:
                if not dontAppend:
                    result+=line[letterIndex]
                letterIndex += 1
            while letterIndex < lineSize-1:
                # print(line[letterIndex])
                
                if line[letterIndex] == '/':
                    if line[letterIndex+1] == '/':
                        if not dontAppend:
                            singleFound = True
                            break
                    elif line[letterIndex+1] == '*':
                        if not dontAppend:
                            dontAppend = True
                            letterIndex += 1
                    else:
                        if not dontAppend:
                            result+=line[letterIndex]
                    letterIndex += 1
                        
        
                elif line[letterIndex] == '*':
                    if dontAppend:
                        if line[letterIndex+1] == '/':  
                            dontAppend = False
                            letterIndex += 1  
                            # print("closed")
                            if letterIndex == lineSize-1 and not(line[letterIndex-1] =="*" or  line[letterIndex-1] =="/"):
                                result+=line[letterIndex]
                        
                    else:
                        result+=line[letterIndex]
                        # print("added",line[letterIndex])
                    
                    letterIndex += 1
               
                else:
                    if not dontAppend:
                        result+=line[letterIndex]
                    letterIndex += 1
                if letterIndex == lineSize-1 and not dontAppend and not singleFound:
                    
                    result+=line[letterIndex]
            
            
            if not dontAppend:
                result+="\n"
                    
                     
            # print(dontAppend,result)
            newList = []
            for data in list(result.split('\n')):
                if data != '':
                    newList.append(data)
        
        
        return newList
                    