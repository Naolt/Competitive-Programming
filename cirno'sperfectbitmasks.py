t = int(input())

def find(n,one):
    mask = 1
    if one:
    	while (n & mask) == 0:
            mask <<= 1
    else:
        while (n & mask) == 1:
            mask <<= 1
            
    return mask

for _ in range(t):
    n = int(input())
    mask = find(n,True)
    if n ^ mask == 0:
        mask = (mask|find(n,False))
    print(mask)