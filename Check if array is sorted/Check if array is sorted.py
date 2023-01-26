class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                return False
        return True

