if __name__ == '__main__':
    n = int(input())
    numList = tuple(map(int, input().split()))
 
    print(hash(numList))
