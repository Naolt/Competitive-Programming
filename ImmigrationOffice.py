n = int(input())
names = list(input().split())
q = int(input())
 
for i in range(q):
    name = input()
    left = -1
    right = len(names)
    while left + 1 < right:
        mid = left + (right-left)//2
        if names[mid] <= name:
            left = mid
        else:
            right = mid
    print(left + 1)