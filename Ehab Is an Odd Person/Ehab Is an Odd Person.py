n = int(input())
nums = list(map(int,input().split()))

foundEven = False
foundOdd = False

for num in nums:
	if num % 2 == 0:
		foundEven = True
	else:
		foundOdd = True

if foundOdd and foundEven:
	nums.sort()
	
print(*nums)
