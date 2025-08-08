class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        count = 0
        numDic = defaultdict(list)
        for idx,val in enumerate(nums):
            for j in numDic[val]:
                if (idx * j) % k == 0:
                    count += 1 
            numDic[val].append(idx)    
        

        return count

        