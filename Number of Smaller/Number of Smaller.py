n,m = map(int,input().split())

num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
result = []
first = second = 0
count = 0

while second < m and first < n:
    
	if num1[first] < num2[second]:
		count += 1
		first += 1
	else:
		result.append(count)
		second += 1

if second < m:
	for i in range(second,m):
		result.append(count)

print(*result)

