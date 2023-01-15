# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(lambda:[])
sizes = input().split()
n,m = int(sizes[0]), int(sizes[1])


grpB = {}

for i in range(n):
    letter = input()
    d[letter].append((i+1))
    
for i in range(m):
    letter = input()
    
    if not d[letter]:
        print(-1)
    else:
        print(*d[letter])

