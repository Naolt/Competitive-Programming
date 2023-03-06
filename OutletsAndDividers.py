import itertools
t = int(input())
 
for _ in range(t):
    n,m = list(map(int,input().split()))
    dividers = list(map(int,input().split()))
    dividers.sort(reverse=True)
    prefix = [1,1]
    for numOfoutlets in dividers:
        prefix.append(numOfoutlets-1)
    #print(prefix)
    prefix = list(itertools.accumulate(prefix))
    found = -1
    for index,value in enumerate(prefix):
        #print(value,index,prefix)
        if value >= n:
            found = index
            break
    if found == 0 or found == 1:
        print(0)
    elif found == -1:
        print(-1)
    else:
        print(found-1)
	