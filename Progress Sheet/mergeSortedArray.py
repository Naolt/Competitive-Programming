"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Input: nums1 = [1,2,2,3,0,0], m = 3, nums2 = [2,5,6], n = 3
Input: nums1 = [1,2,2,3,0,0], m = 3, nums2 = [2,5,6], n = 3
                        i                       j
                       

k = 3+0-2= 1

"""


class Solution:
    def merge(self, num1: List[int], m: int, num2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        k = 0
        
        while j < n:
            #
            if i > m-1+j:
                while i < m + n:
                    num1[i] = num2[j]
                    i+=1
                    j+=1
            else:
                if(num1[i]>num2[j]):
                    k = m+j-i
                    while(k > 0):
                        num1[i+k] = num1[i+k-1]
                        k -= 1
                    num1[i] = num2[j]
                    j+=1
                    i+=1
                else:
                    i+=1
