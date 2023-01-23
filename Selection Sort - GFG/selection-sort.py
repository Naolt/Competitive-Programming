#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        size = len(arr)
        minIndex = i
        for i in range(i,size):
            if arr[i] < arr[minIndex]:
                minIndex = i
        return minIndex
    
    def selectionSort(self, arr,n):
        #code here
      
        for i in range(1,n):
            index = self.select(arr,i)
            if arr[index] < arr[i-1]:
                arr[i-1],arr[index] = arr[index],arr[i-1]
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends