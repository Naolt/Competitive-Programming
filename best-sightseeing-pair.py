class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        cur = res = 0
        for val in values:
            res = max(res, cur + val)
            cur = max(cur, val) - 1
        return res