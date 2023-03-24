class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = self.quickSort(nums,0,len(nums)-1)
        return result[-k]
    def quickSort(self,arr,left,right):
        # print(left,right)
        if left >= right:    
            return arr
        pivot = arr[right]
        write = left-1

        for i in range(left,right):
            if arr[i] <= pivot:
                write += 1
                arr[write],arr[i] = arr[i],arr[write]
        
        arr[write+1],arr[right] = arr[right],arr[write+1]
        # print(arr,write+1)
        self.quickSort(arr,left,write)
        self.quickSort(arr,write+2,right)

        return arr