sizeDict = {"X":10,"S":-1,"L":1,"M":0}
def compare(str1,str2):
    str1Parsed = sizeDict[str1[-1]] * len(str1)
    str2Parsed = sizeDict[str2[-1]] * len(str2)
    
    if str1Parsed > str2Parsed:
        print(">")
    elif str2Parsed > str1Parsed:
        print("<")
    else:
        print("=")
        
        
tests = int(input())
for i in range(tests):
    sizes = input().split()
    compare(sizes[0],sizes[1])
    
    
