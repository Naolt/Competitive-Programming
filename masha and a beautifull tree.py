
def merge(arr1, arr2):
    i = j = 0
    size1= len(arr1[0])
    size2 = len(arr2[0])
    result =  []
    swapped = False
    swap2 = False
    found = 0

    while(i < size1 and j < size2):
        if arr1[0][i] > arr2[0][j]:
            result.append(arr2[0][j])
            j += 1
            swapped = True
        else:
            swap2 = True
            result.append(arr1[0][i])
            i += 1
    result.extend(arr1[0][i:])
    result.extend(arr2[0][j:])
    if swapped:
        found = 1
    if (swapped and swap2) or arr1[1] == -1 or arr2[1] == -1:
        return [result,-1]
    return [result,found+arr1[1]+arr2[1]]


def mergeSort(arr,left,right):
    if left == right:
        return [[arr[left]],0]
    middle = left + (right-left)//2
    leftArr = mergeSort(arr,left,middle)
    rightArr = mergeSort(arr,middle+1,right)
    return merge(leftArr,rightArr)
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    arr,moves = mergeSort(nums,0,n-1)
    #print(arr,moves)
    if arr[-1] > n:
        print(-1)
    else:
        print(moves)