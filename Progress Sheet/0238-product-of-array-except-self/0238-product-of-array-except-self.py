class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        a= nums
        prod = 1
        flag = 0
        
        for i in range(n):
            if (a[i] == 0):
                flag += 1
            else:
                prod *= a[i]
        # Creating a new array of size n
        arr = [0 for i in range(n)]
        
        for i in range(n):
            # If number of elements in
            # array with value 0
            # is more than 1 than each
            # value in new array
            # will be equal to 0
            
            if (flag > 1):
                arr[i] = 0
            # If no element having value
            # 0 than we will
            # insert product/a[i] in new array
            
            elif (flag == 0):
                arr[i] = (prod // a[i])
            
            # If 1 element of array having
            # value 0 than all
            # the elements except that index
            # value , will be
            # equal to 0
            
            elif (flag == 1 and a[i] != 0):
                arr[i] = 0
            else:
                arr[i] = prod
        return arr
