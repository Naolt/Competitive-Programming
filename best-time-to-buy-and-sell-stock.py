class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        val = 0
        minimum = float("inf")
        for price in prices:
            minimum = min(minimum, price)
            val = max(val, price - minimum)
        return val