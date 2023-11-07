class Solution:
    def countOfAtoms(self, formula: str) -> str:
        

        def getElem(index):
            if index >= len(formula):
                return len(formula)
            char = formula[index]
            while index < len(formula) and char.isalpha() and char.islower():
                index += 1
                if index < len(formula):
                    char = formula[index]
            return index

        def getNum(index):
            if index >= len(formula):
                return len(formula)
            char = formula[index]
            while index < len(formula) and char.isdigit():
                index += 1
                if index < len(formula):
                    char = formula[index]
            return index


        stack = []
        i = 0

        while i < len(formula):
            char = formula[i]
            if char.isalpha() and formula[i].isupper():
                elemIndex = getElem(i+1)
                element = formula[i:elemIndex]
                numIndex = getNum(elemIndex) 
                number = formula[elemIndex:numIndex]
                
                if number == "":
                    number = 1
                    i = numIndex
                else:
                    number = int(number)
                    i = numIndex
                stack.append((element,number))
            else:
                if char == ')':
                    numIndex = getNum(i+1)
                    number = formula[i+1:numIndex]
                    if number == "":
                        number = 1
                        i = numIndex
                    else:
                        number = int(number)
                        i = numIndex
                    popped = []
                    while stack and stack[-1][0] != '(':
                        elem,count = stack.pop()
                        popped.append((elem,count*number)) 
                    
                    if stack:
                        stack.pop()
                    stack.extend(popped)
                else:
                    stack.append((char,0))
                    i += 1

        numDict = defaultdict(int)
        for e,c in stack:
            numDict[e] += c
        
        sortedKeys = sorted(numDict)
        answer = ""
        for e in sortedKeys:
            answer += e
            if numDict[e] > 1:
                answer += str(numDict[e])

        return answer
        
