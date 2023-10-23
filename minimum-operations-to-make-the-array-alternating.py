class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        size = len(nums)
        even,odd = defaultdict(int),defaultdict(int)
        evenCount,oddCount = (size//2,size//2) if size % 2 == 0 else (size//2+1,(size//2))

        for i in range(0,size,2):
            even[nums[i]] += 1            
            if i < size-1:
                odd[nums[i+1]] += 1

        evenNums = list(even.items())
        oddNums = list(odd.items())
        oddNums.append((-1,0))
        evenNums.append((-1,0))
        evenNums.sort(key=lambda x:x[1])
        oddNums.sort(key=lambda x:x[1])

        cost = 0

        
        cost1,cost2 = inf,inf
        
        cost1 = evenCount - evenNums[-1][1]
        if evenNums[-1][0] == oddNums[-1][0]:
            cost1  += (oddCount - oddNums[-2][1])
        else:
            cost1  += (oddCount - oddNums[-1][1])
        
        cost2 = oddCount - oddNums[-1][1]
        if evenNums[-1][0] == oddNums[-1][0]:
            cost2  += (evenCount - evenNums[-2][1])
        else:
            cost2  += (evenCount - evenNums[-1][1])

        cost = min(cost1,cost2)


        
        return cost


                





        return 0