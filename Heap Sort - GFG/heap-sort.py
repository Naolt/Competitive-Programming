#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, current):
        # code here
        smallest = arr[0]
        self.Swap(arr,0,len(arr)-1)
        arr.pop()
        
        leftIndex = self.LeftChild(arr,current)
        rightIndex = self.RightChild(arr,current)
        
        while  (leftIndex < n and arr[leftIndex] < arr[current]) or (rightIndex < n and arr[rightIndex] < arr[current]):

            if leftIndex < n and rightIndex < n:
                
                if arr[leftIndex] < arr[rightIndex]:
                    self.Swap(arr,leftIndex,current)
                    current = leftIndex
                else:
                    self.Swap(arr,rightIndex,current)
                    current = rightIndex
            else:
                self.Swap(arr,leftIndex,current)
                current = leftIndex
           
            leftIndex = self.LeftChild(arr,current)
            rightIndex = self.RightChild(arr,current)
        
        return smallest
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        heap = []
        for num in arr:
            heap.append(num)
            self.heapifyUp(heap,len(heap)-1)
        return heap
    
    def heapifyUp(self,heap,current):
        parent = self.parent(heap,current)
        if current > 0 and heap[parent] > heap[current]:
            self.Swap(heap,current,parent)
            self.heapifyUp(heap,parent)
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        heap = self.buildHeap(arr,len(arr))
        # print(heap)
        result = []
        size = len(heap)
        for i in range(size):
            smallest = self.heapify(heap,len(heap)-1,0)
            arr[i]=smallest
    
    def LeftChild(self,arr,i):
        return 2*i + 1
    def RightChild(self,arr,i):
        return 2*i + 2
    def parent(self,arr,i):
        return (i-1)//2
    def Swap(self,heap,parent,current):
        heap[parent] , heap[current] = heap[current] , heap[parent]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends