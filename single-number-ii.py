class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            nums[i] += 2**31
        answer = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num & (1 << i))
            if count%3:
                answer |= (1 << i)

        return answer-2**31