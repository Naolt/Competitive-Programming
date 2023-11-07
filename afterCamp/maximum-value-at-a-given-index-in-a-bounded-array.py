class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def getValue(value):
            totLeft,totRight = 0,0
            leftSize = index
            rightSize = n - 1 - index
            
            totRight += value*(value+1)//2
            totLeft += value*(value+1)//2
            if value > leftSize:
                temp = value-leftSize
                totLeft -= temp*(temp+1)//2
            elif value <= leftSize:
                totLeft += leftSize-value
            
            if value > rightSize:
                temp = value-rightSize
                totRight -= temp*(temp+1)//2
            elif value <= rightSize:
                totRight += rightSize-value

            return totLeft+totRight


        low = 1
        high = maxSum

        while low < high:
            middle = low + (high-low)//2
            total = getValue(middle-1)
            if total+middle <= maxSum:
                low = middle+1
            else:
                high = middle

        res = getValue(low-1)+low
    
        return low-1 if res > maxSum else low