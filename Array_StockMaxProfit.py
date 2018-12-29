import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minPrice = sys.maxint
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit


# Dynamic programming solution
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """

#         if len(prices) == 0:
#             return 0

#         dp = [None] * len(prices)
#         dp[0] = prices[0]
#         profit = 0

#         for i in range(1, len(prices)):
#             profit = max(prices[i] - dp[i-1], profit)
#             dp[i] = prices[i] if prices[i] < dp[i-1] else dp[i-1]

#         return profit

