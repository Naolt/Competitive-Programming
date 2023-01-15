# Enter your code here. Read input from STDIN. Print output to STDOUT
noOfEnglish = int(input())
englishList = list(map(int,input().split()))
noOfFrench = int(input())
frenchList = list(map(int,input().split()))

print(len(set(englishList).difference(frenchList)))

