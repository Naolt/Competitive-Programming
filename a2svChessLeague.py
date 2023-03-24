
def IL(): return list(map(int,input().split()))
def ILS(): return sorted(list(map(int,input().split())))
def SL(): return list(input().split())
def SLS(): return sorted(list(input().split()))
def I(): return int(input())
def S(): return input()


def mergeSort(left,right,arr,k):
    if left == right:
        return [arr[left]]
    middle = left + (right - left)//2
    leftArr = mergeSort(left,middle,arr,k)
    rightArr = mergeSort(middle+1,right,arr,k)
    winnersLeft,winnersRight = getWinners(leftArr,rightArr,k)
    return merge(winnersLeft,winnersRight)
def getWinners(arr1, arr2,k):
    i = j = 0
    size1= len(arr1)
    size2 = len(arr2)
    while i < size1 and j < size2:
        if arr1[i][0] - arr2[j][0] > k:
            j += 1
        elif arr2[j][0] - arr1[i][0] > k:
             i += 1
        else:
            break
    return [arr1[i:],arr2[j:]]
            

def merge(arr1, arr2):
    i = j = 0
    size1= len(arr1)
    size2 = len(arr2)
    result =  []

    while(i < size1 and j < size2):
        if arr1[i][0] > arr2[j][0]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

n,k = IL()
nums = IL()
newNums = []
for index,num in enumerate(nums):
    newNums.append((num,index))
    
result = mergeSort(0,len(newNums)-1,newNums,k)
answer = list(map(lambda key:key[1]+1,sorted(result,key=lambda key: key[1])))
print(*answer)