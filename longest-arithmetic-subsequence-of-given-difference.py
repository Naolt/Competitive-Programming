class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        memo = defaultdict(int)

        for num in arr:
            target = num - difference
            if target in memo:
                memo[num] = memo[target] + 1
            else:
                memo[num] = 1
        return max(memo.values())