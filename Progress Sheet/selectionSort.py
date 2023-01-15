
class Solution:
	def select(self, arr, i):
		print(arr,i)
		
		min = i
		for j in range(i+1,len(arr)):
			if(arr[j]<arr[min]):
				min = j
		print(min)
		return min
	def selectionSort(self, arr,n):
		if(not(n >= 1 and n <= 10**3)):
			return
		for j in range(len(arr)):
			selected = self.select(arr,j)

			if(selected != j):
				temp = arr[selected]
				arr[selected] = arr[j]
				arr[j] = temp
		return arr


array = Solution()
print(array.selectionSort([1,4,5,2,9,0],1000))
