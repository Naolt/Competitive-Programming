"""
if length of other set without setA is greater than 0 return false

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int,input().split()))
noOfSets = int(input())
flag = True

for i in range(noOfSets):
    otherSet = set(map(int,input().split()))
    
    if len(otherSet - setA) > 0:
        flag = False
        break
print(flag)

