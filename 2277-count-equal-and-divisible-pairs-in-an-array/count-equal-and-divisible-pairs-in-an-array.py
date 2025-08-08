class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        count = 0
        for idx,val1 in enumerate(nums):
            for i in range(idx+1,len(nums)):
                val2 = nums[i]

                if val1 == val2 and (idx * i) % k == 0:
                    count += 1

        return count

        