tests = int(input())




for i in range(tests):
    i = 0
    j = 1
    cost = 0
    [n,c] = list(map(int,input().split()))
    planets = list(map(int,input().split()))
    planets.sort()
    
    if n == 1:
        cost = 1
    
    while j < n:
        
        if(planets[i] == planets[j]):
            j += 1
        elif planets[i] != planets[j]:
            if j-i < c:
                cost += (j-i)
                # print("added",cost)
            else:
                cost += c
            i = j
            j = i+1
        if j == n:
            if j-i < c:
                cost += (j-i)
            else:
                cost += c
            
    print(cost)
        
