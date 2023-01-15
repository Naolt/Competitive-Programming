"""

 set(a,b,c) set(a,d,c)
     b,c 2          d,c
     1

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

noOfEnglish = int(input())
englishList = set(map(int,input().split()))
noOfFrench = int(input())
frenchList = set(map(int,input().split()))

print(len(englishList|frenchList))
