class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        key = None
        value = None
        ans = []
        for i in range(size):
            ans.append(nums[nums[i]])

        return ans
                