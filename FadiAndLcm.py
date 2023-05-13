import math
x = int(input())
 
def getFactors(n):
    dic = {}
    for i in range(1,int(n**0.5)+1):
       if math.gcd(i,n//i) == 1 and i*(n//i )== n:
           dic[max(i,n//i)] = [i,n//i]
    return dic[sorted(dic)[0]]
 
print(*getFactors(x))