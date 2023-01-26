n,m = map(int,input().split())

num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))

first = 0
second = 0
result = []

while first < n and second < m:
    if num1[first] < num2[second]:
        result.append(num1[first])
        first += 1
    else:
        result.append(num2[second])
        second += 1

if first < n:
    result.extend(num1[first::])
if second < m:
    result.extend(num2[second::])
    
print(*result)
