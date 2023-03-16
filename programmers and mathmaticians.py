t = int(input())

for _ in range(t):
    a,b = list(map(int,input().split()))
    calc = (a+b)//4
    print(min(calc,min(a,b)))
            
        