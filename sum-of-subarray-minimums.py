class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = self.nextSmaller(arr[::-1],True)[::-1]
        right = self.nextSmaller(arr,False)
        size = len(arr)
        result = 0
        print(left,right)

        for index,num in enumerate(arr):
            numsLeft = index - (size-left[index]-1) - 1
            if left[index] == -1:
                numsLeft = index
            numsRight = right[index] - index -1
            if right[index] == -1:
                numsRight = size - index - 1
            result += ((numsLeft+1)*(numsRight+1)*num)
            print((index,num),numsLeft,numsRight)
        return result%(10**9+7)
    def nextSmaller(self,arr,left):
        stack = []
        dic = {}
        size = len(arr)
        result = [-1]*size
        for index,num in enumerate(arr):

                while stack and ((left and stack[-1][0] > num )or ( not left and stack[-1][0] >= num)):
                    dic[stack.pop()[1]] = index
                stack.append((num,index))


        for key,value in dic.items():
            result[key] = value        
        return result