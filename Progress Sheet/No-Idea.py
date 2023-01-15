# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = list(map(int,input().split()))
array = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
happy = 0


for i in array:
    if i in a:
        happy +=1
    if i in b:
        happy -=1
print(happy)
