class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        res = 1
        sum_ = nums[0]
        total = nums[0]
        for num in nums:
            total &= num
        print(total)
        for i in range(len(nums)):
            sum_ &= nums[i]
            print(sum_)
            if sum_ == total == 0:
                res += 1
                if i < len(nums)-1:
                    sum_ = nums[i+1]
        return res if total != 0 else res -1