class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        result = self.mergeSort(0,len(nums)-1,nums)
        return result[1]
    def mergeSort(self,left,right,arr):
        if left == right:
            return [[arr[left]],0]
        middle = left + (right - left)//2
        leftArr = self.mergeSort(left,middle,arr)
        rightArr = self.mergeSort(middle+1,right,arr)
        merged = self.merge(leftArr[0],rightArr[0])
        return [merged,self.checkPair(leftArr,rightArr)+leftArr[1]+rightArr[1]]
    def merge(self,arr1, arr2):
        i = j = 0
        size1= len(arr1)
        size2 = len(arr2)
        result =  []

        while(i < size1 and j < size2):
            if arr1[i] > arr2[j]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr1[i])
                i += 1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result

    def checkPair(self,arr1,arr2):
        i = 0
        j = 0
        size1 = len(arr1[0])
        size2 = len(arr2[0])
        count = 0        
        while(i < size1 and j < size2):
            if arr1[0][i] > 2*arr2[0][j]:
                count += size1-i
                j += 1
            else:
                i += 1
        return count