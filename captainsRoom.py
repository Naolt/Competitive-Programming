# Enter your code here. Read input from STDIN. Print output to STDOUT
def findCaptain(k,l):
    l = list(l)
    l.sort()
    first = 0
    last = k-1
    room = -1
    while(last<len(l)):
        if(l[first]!= l[first+1]):
            room = l[first]
            break
        elif( l[last] != l[last-1]):
            room = l[last]
            break
        first = last+1
        last = last + k
    if room == -1:
           room = l[first]
    print(room)
        
k = int(input())
l = map(int,input().split())
    
findCaptain(k,l)
