# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
[1,2,3,8,7]
 i     j 

c = j j>i



"""

T = int(input())

for k in range(T):
    size = int(input())
    array = list(map(int,input().split()))
    i = 0
    j = len(array)-1
    start = 0
    ok = True
    while(i != j):
        
        if array[i] > array[j]:
            start = i
            i+=1
            if start != 0 and array[start] < array[i]:
                ok = False
                break
                
        else:
            start = j
            j-=1
            if start != 0 and array[start] < array[j]:
                ok = False
                break
    if ok:
        print("Yes")
    else:
        print("No")
