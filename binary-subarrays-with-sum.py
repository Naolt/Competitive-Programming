class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        dic = defaultdict(int)
        dic[0] = 1
        prefix = list(accumulate(nums))
        result = 0
        print(prefix)
        for num in prefix:
            if num - goal in dic:
                result += dic[num-goal]
            dic[num] += 1

        return result