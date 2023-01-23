from collections import defaultdict
[n,m] = list(map(int,input().split()))
result = []
answer = ""
result = []
for i in range(n):
    line = list(input())
    result.append(line)
    

    
for i in range(n):
    for j in range(m):
        elem = result[i][j]
        found = False
        # check row:
        for k in range(m):
            
            if elem == result[i][k] and k != j:
                
                found = True
                break
        if not found:
            
            # check column
            for k in range(n):
                
                if elem == result[k][j] and k != i:
                    found = True
                    break
        if not found:
            answer += elem
        
print(answer)


"""
time Complexity = O(n*m*n)
space Complexity = O(1)
"""
