class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        size = len(nums)
        prefix = [0]*(size+1)

        for [start,end] in requests:
            prefix[start] += 1
            prefix[end+1] -= 1
        prefix = list(accumulate(prefix))
        prefix.sort(reverse=True)
        nums.sort(reverse = True)
        result = 0
        for i in range(size):
            if prefix[i]:
                result += (prefix[i]*nums[i])
            else:
                break
        return result%((10**9)+7)