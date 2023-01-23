tests = int(input())
 
for _ in range(tests):
    size = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    found = False
    
    for i in range(1,size):
        if nums[i]-nums[i-1] > 1:
            found = True
            break
    if found:
        print("NO")
    else:
        print("YES")
